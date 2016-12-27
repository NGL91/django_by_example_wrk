
#Output json data in courses
python manage.py dumpdata courses --indent=2 --ouput=courses/fixtures/subjects.json


#Load data from json files in fixtures folder into database
python manage.py loaddata subjects.json

#Run memcached
memcached -l 127.0.0.1:11211

#Install django memcached status
pip install git+git://github.com/zenx/django-memcache-status.git