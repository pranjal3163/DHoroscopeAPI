# DHoroscopeAPI
An application built in using django with scrappy. Intregation of django and scrapy using scrapyd  

# Set up

* Create a virtual environment and activate it:

  python -m venv venv 
  source venv/bin/activate
* install requirements
  pip install -r requirements.txt
  
* create django app

  django-admin startproject DHoroscopeCrawler
  cd DHoroscopeCrawler && python manage.py startapp main

* create scrapy app
  
  cd DHoroscopeCrawler
  scrapy startproject scrapy_dhoroscope

database
  
  python manage.py makemigrations

  python manage.py migrate



* run django
 python manage.py runserver

* run scrapyd

  cd scrapy_dhoroscope

  scrapyd
  
  curl http://localhost:6800/schedule.json -d project=default -d spider=hcrawler
