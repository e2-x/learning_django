import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

## Fake pop script
import random
from second_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fake_gen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def add_user():
    fake_user_name = fake_gen.name()
    fake_user_email = fake_gen.email()

    f_name = fake_user_name.split()[0]
    l_name = fake_user_name.split()[1]
    user = User.objects.get_or_create(first_name=f_name, last_name=l_name, email_address=fake_user_email)[0]
    user.save()

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()
        add_user()

        # Create the fake data for that entry
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('Populating script')
    populate(20)
    print('Populating complete')
