import os.path
import pytest
from WordleAPI import CorpusBase


class TestClass:

    def test_one(self):
        """Captura de un fichero de texto de prueba"""
        c = CorpusBase(os.path.join("txt", "test.txt"))
        assert(isinstance(c, CorpusBase))
        assert(c.origen == os.path.join("txt", "test.txt"))
        assert(c.num_lineas == 11)
        assert(c.num_palabras == 10)
        assert(c.corpus[0] == ('sobre', 1))
        assert(len(c.lista) == 10)
        assert(c.word_size == 5)
        assert(c.exists('tiene'))
        assert(c.exists('madre') is False)
        assert(c.pick()[0] in c.lista)
        assert(len(c.pick(5)) == 5)
        assert(len(c.pick(10)) == 10)
        with pytest.raises(ValueError):
            len(c.pick(15)) == 10

    def test_two(self):
        """Captura de un texto que incluye frecuencias
        y cancelación de caracteres con acentos"""
        fich = os.path.join("txt", "test2.txt")
        p1 = r"\('(\w+).+"
        p2 = r"\('\w+', (\d+\.\d+)\)"
        xg = [('í', 'i')]
        c = CorpusBase(fich, pattern=p1, pattern_freq=p2, list_char_conversion=xg)
        assert(isinstance(c, CorpusBase))
        assert(c.corpus[2] == ('habia', 1464.55, 'había'))
        assert(c.corpus[-1] == ('donde', 865.74))
        assert(c.exists('había') is False)
