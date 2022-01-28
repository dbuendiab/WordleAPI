from WordleAPI.corpus_read import CorpusBase
from WordleAPI import Corpus


def test_esp():
    """Fichero en español"""
    c = Corpus.español()
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == 'txt\\CREA_total.TXT')
    assert(c.num_lineas == 737800)
    assert(c.num_palabras == 737797)
    assert(c.corpus[0] == ('sobre', 1898.97))
    assert(c.corpus[-1] == ('zylox', 0.0))
    assert(len(c.lista) == 50152)
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
    c = Corpus.ingles()
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == 'txt\\words_alpha.txt')
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
    c = Corpus.catalan()
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == 'txt\\paraules_cat.txt')
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
    c = Corpus.español(word_size=8)
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == 'txt\\CREA_total.TXT')
    assert(c.num_lineas == 737800)
    assert(c.num_palabras == 737797)
    assert(c.corpus[0] == ('gobierno', 740.77))
    assert(c.corpus[-1] == ('zzzzzzzz', 0.0))
    assert(len(c.lista) == 100714)
    assert(c.word_size == 8)
    assert(c.exists('desocupa'))
    assert(c.exists('pppppppp') is False)
    assert(c.pick()[0] in c.lista)
    assert(len(c.pick(5)) == 5)
    assert(len(c.pick(10)) == 10)


def test_ing11():
    """Fichero en ingles"""
    c = Corpus.ingles(word_size=11)
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == 'txt\\words_alpha.txt')
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
    c = Corpus.catalan(word_size=3)
    assert(isinstance(c, Corpus))
    assert(isinstance(c, CorpusBase))
    assert(c.origen == 'txt\\paraules_cat.txt')
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
