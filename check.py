from importlib import util
if util.find_spec("psycopg2"):
    print("psycopg2 is installed")
else:
    print("psycopg2 is not installed")