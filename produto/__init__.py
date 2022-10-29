import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetos.settings")
import string
import timeit
from random import choice, random, radint
from produto.models import Produto

class Utils:
    """ Metodos Genericos"""
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits)for i in range(max_length)))