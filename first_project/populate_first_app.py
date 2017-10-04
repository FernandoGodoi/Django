import os

#configura o projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random

from first_app.models import Topic, Webpage, AccessRecord

from faker import Faker

fakegen = Faker()
topicos = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topicos))[0]
    t.save()
    return t

def populate(N=5):
    '''
    Cria N entradas em paginas e acessos
    '''

    for entry in range(N):

#pega o topico para Entry
        top = add_topic()

#cria dados fake para entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

#cria uma nova entrada em paginas (Webpage)
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name= fake_name)[0]

# cria registros de acesso (AccessRecord)
        accRec = AccessRecord.objects.get_or_create(pagina=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populando o banco de dados... Por favor espere")
    populate(20)
    print('Banco de dados populado.')