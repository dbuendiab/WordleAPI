import os.path
from WordleAPI.corpus_read import CorpusBase
from WordleAPI import Corpus

ruta_ing = os.path.join("txt", "words_alpha.txt")
ruta_esp = os.path.join("txt", "palabra2.txt")
ruta_cat = os.path.join("txt", "paraules_cat.txt")

def test_esp():
    """Fichero en español"""
    c = Corpus.esp()
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == ruta_esp)
    assert(c.num_lineas == 61054)
    assert(c.num_palabras == 61054)
    assert(c.corpus[0] == ('alesi', 0.51))
    assert(c.corpus[-1] == ('sobre', 1898.97))
    assert(len(c.lista) == 5040)
    assert(c.word_size == 5)
    assert(c.exists('tiene'))
    assert(c.exists('mkkkk') is False)
    assert(c.pick()[0] in c.lista)
    assert(len(c.pick(5)) == 5)
    assert(len(c.pick(10)) == 10)
    assert(c.find('habia') == {('habia', 0.74), ('habia', 1464.55, 'había')})
    assert(c.find('había') == {('habia', 1464.55, 'había')})


def test_ing():
    """Fichero en ingles"""
    c = Corpus.ing()
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == ruta_ing)
    assert(c.num_lineas == 370103)
    assert(c.num_palabras == 370103)
    assert(c.corpus[0] == ('aahed', 1))
    assert(c.corpus[-1] == ('zunis', 1))
    assert(len(c.lista) == 15918)
    assert(c.word_size == 5)
    assert(c.exists('where') is True)
    assert(c.exists('tiene') is False)
    assert(c.pick()[0] in c.lista)
    assert(len(c.pick(5)) == 5)
    assert(len(c.pick(10)) == 10)


def test_cat():
    """Fichero en catalán"""
    c = Corpus.cat()
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == ruta_cat)
    assert(c.num_lineas == 65843)
    assert(c.num_palabras == 65843)
    assert(c.corpus[0] == ('abaca', 1))
    assert(c.corpus[-1] == ('zonat', 1))
    assert(len(c.lista) == 4169)
    assert(c.word_size == 5)
    assert(c.exists('tarda') is True)
    assert(c.exists('tiene') is False)
    assert(c.pick()[0] in c.lista)
    assert(len(c.pick(5)) == 5)
    assert(len(c.pick(10)) == 10)


def test_esp8():
    """Fichero en español"""
    c = Corpus.esp(word_size=8)
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == ruta_esp)
    assert(c.num_lineas == 61054)
    assert(c.num_palabras == 61054)
    assert(c.corpus[0] == ('abonando', 0.51))
    assert(c.corpus[-1] == ('gobierno', 740.77))
    assert(len(c.lista) == 9612)
    assert(c.word_size == 8)
    assert(c.exists('friburgo'))
    assert(c.exists('pppppppp') is False)
    assert(c.pick()[0] in c.lista)
    assert(len(c.pick(5)) == 5)
    assert(len(c.pick(10)) == 10)


def test_ing11():
    """Fichero en ingles"""
    c = Corpus.ing(word_size=11)
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == ruta_ing)
    assert(c.num_lineas == 370103)
    assert(c.num_palabras == 370103)
    assert(c.corpus[0] == ('abacination', 1))
    assert(c.corpus[-1] == ('zugtierlast', 1))
    assert(len(c.lista) == 37539)
    assert(c.word_size == 11)
    assert(c.exists('imperatrice') is True)
    assert(c.exists('perpirporpu') is False)
    assert(c.pick()[0] in c.lista)
    assert(len(c.pick(5)) == 5)
    assert(len(c.pick(10)) == 10)


def test_cat3():
    """Fichero en catalán"""
    c = Corpus.cat(word_size=3)
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == ruta_cat)
    assert(c.num_lineas == 65843)
    assert(c.num_palabras == 65843)
    assert(c.corpus[0] == ('aci', 1))
    assert(c.corpus[-1] == ('zoo', 1))
    assert(len(c.lista) == 547)
    assert(c.word_size == 3)
    assert(c.exists('mar') is True)
    assert(c.exists('ole') is False)
    assert(c.pick()[0] in c.lista)
    assert(len(c.pick(5)) == 5)
    assert(len(c.pick(10)) == 10)
