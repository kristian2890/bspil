# Generated by Django 4.1.4 on 2023-05-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spil", "0006_alter_home_home_id_alter_score_priceguess"),
    ]

    operations = [
        migrations.AlterField(
            model_name="score",
            name="priceguess",
            field=models.DecimalField(
                decimal_places=1,
                default=0,
                max_digits=20,
                verbose_name="Hvad tror du boligens udbudspris er?",
            ),
        ),
    ]
