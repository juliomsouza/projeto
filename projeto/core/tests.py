from django.test import TestCase
from projeto.core.models import Produtos


class ModelProdutosTest(TestCase):
    def test_create(self):
        self.obj = Produtos.objects.create(name='cerveja', description='antartica')
        self.assertTrue(Produtos.objects.exists())
