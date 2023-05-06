from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import * 
from .forms import ScoreForm, CustomUserForm
from django.contrib.auth import login, authenticate, logout
from django.db.models import Prefetch, F, Sum, Count, DecimalField, FloatField
from django.db.models.functions import Abs, Cast

def index(request):

    homescores = Home.objects.prefetch_related().filter(scores__user__isnull=False).order_by('-scores__ucreated_at')[:1] 
    context = {'homescores' : homescores}

    return render(request, 'index.html', context)

def bolig(request):
    
    hometest = Home.objects.prefetch_related().exclude(scores__user__exact=request.user)[:1] #.filter(scores__user__isnull=True)
    
    if request.method == "POST":
        form = ScoreForm(request.POST)
        if form.is_valid():
            scoreformsave = form.save(commit=False)
            scoreformsave.user = request.user
            scoreformsave.home = hometest[0]
            scoreformsave.save()
            return redirect('post_bud')
    
    form = ScoreForm()
    #imagetest = Home.objects.select_related('image').all()
    
    #if there are no home objects in hometest then return bolig404 template instead 
    if not hometest:
        return render(request, 'bolig404.html')
    else:
        return render(request, 'bolig.html' , {'homes': hometest, 'form':form})

def register_page(request):
    
    if request.user.is_authenticated:
        return redirect('accounts/logout/')

    if request.method != 'POST':
        form = CustomUserForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/login/')



def post_bud(request):
    home_info = Home.objects.prefetch_related().filter(scores__user__exact=request.user).order_by('-scores__created_at')[:1]
    scores_info = Score.objects.prefetch_related().filter(user__exact=request.user).order_by('-created_at')[:1]
    home_difference = home_info.annotate(diff=F('pris') - F('scores__priceguess'))
    context = {'home_info' : home_info, 'home_difference':home_difference, 'scores_info':scores_info}
    return render(request, 'post_bud.html', context)
     
def bolig404(request):

    return render(request, 'bolig404.html')
             
    
def highscore(request):
    #count = list(range(Home.objects.prefetch_related().filter(scores__user__exact=request.user).order_by('-scores__created_at').count()))
    high_home_info = Home.objects.prefetch_related().filter(scores__user__exact=request.user).order_by('-scores__created_at')
    high_scores_info = Score.objects.prefetch_related().filter(user__exact=request.user).order_by('-created_at')
    
    result = Score.objects.prefetch_related().values('user__username').annotate(total_homes =Count('home_id'), total_priceguess=Sum('priceguess'), total_difference=Sum(Abs(F('home__pris') - F('priceguess'))), avg_difference=(Sum(Abs(F('home__pris') - F('priceguess'))) / Count('home_id')), total_price=Sum(F('home__pris')), pct_difference = Cast(F('total_difference'),FloatField())  / Cast(F('total_price'), FloatField())*100).order_by('avg_difference')
    context = {'high_home_info' : high_home_info, 'high_scores_info':high_scores_info, 'result':result}  
    return render(request, 'highscore.html', context)