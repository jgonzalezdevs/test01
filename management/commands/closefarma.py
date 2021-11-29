from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
import requests
from farmacia.models import Mindicador


class Command(BaseCommand):

    help = 'Script que obtiene informacion de una api y las envia por correo.'

    def __init__(self):
        self.respose = ''
        self.resp = ''

    def run(self):
        self.start_request()
        self.print_request()
        self.send_mail()

    def handle(self, *args, **kwargs):
        instance = Command()
        instance.run()

    def start_request(self):
        self.response = requests.get('https://mindicador.cl/api')

    def print_request(self):
        if(self.response.status_code == 200):
            print(self.response.json())
        else:
            print('Error {} en consulta.'.format('self.response.status_code'))

    def save_data(self):
        for objt in self.response.json():
            try:
                obj, created = Mindicador.objects.get_or_create(
                    codigo=''.format(objt['codigo']),
                    nombre=''.format(objt['nombre']),
                    unidad_medida=''.format(objt['unidad_medida']),
                    fecha=''.format(objt['fecha']),
                    valor=''.format(objt['valor'])
                )
            except:
                pass

    def send_mail(self):
        send_mail(
            'Subject here',
            'Here is the message.'.format(self.response),
            ['luis.vergara@sistemasexpertos.cl'],
            fail_silently=False,
        )
