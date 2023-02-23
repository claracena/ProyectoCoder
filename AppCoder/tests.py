from django.test import TestCase
from AppCoder.models import Profesor

# Create your tests here.
class URLTest(TestCase):

    def test_inicio(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class TestModels(TestCase):

    def setUp(self):
        self.profesor1 = Profesor.objects.create(
            nombre = 'Profesor de ejemplo 1',
            apellido = 'Apellido de ejemplo 1',
            email = 'algunemail@email.com',
            profesion = 'Alguna profesion'
        )

    def test_modulo(self):
        self.assertEquals(self.profesor1.nombre, 'Profesor de ejemplo 2')
        self.assertEquals(self.profesor1.apellido, 'Apellido de ejemplo 1')