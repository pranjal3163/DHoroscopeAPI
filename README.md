# DHoroscopeAPI
Api for the mobile app

Set up

install requirements

pip install -r requirements.txt

database
  
  python manage.py makemigrations

  python manage.py migrate



run django
python manage.py runserver

run scrapyd

cd scrapy_dhoroscope

scrapyd

curl http://localhost:6800/schedule.json -d project=default -d spider=crawler
