from WordleAPI.corpus_read import CorpusBase
from WordleAPI import Corpus
from WordleAPI import Search


def test_search():
    """Test de la clase Search, que hace búsquedas en el corpus
    Uso el fichero en español porque es el único que contiene acentos"""
    s = Search.esp()
    assert(isinstance(s, Search))
    assert(isinstance(s, Corpus))
    assert(isinstance(s, CorpusBase))

    ## Filtrar palabras empezando por 'lam'
    def filtro(x):
        return x[0].startswith('lam')

    ## Ordenar alfabéticamente ignorando el primer carácter
    def orden(x):
        return x[0][1:]
    r = s.search(filtro, orden, reverse=True)
    assert(len(r) == 39)
    assert(r[0] == 'lamyr')
    assert(r[-1] == 'laman')

    def filtro(x):
        return x[0].startswith('hab')

    def orden(x):
        return x[0]
    r = s.search(filtro, orden)
    assert(len(r) == 46)
    assert(r[0] == 'habad')
    assert(r[-1] == 'habze')

    assert(s.exists('habla') is True)

    assert(s.regex('.a.o.')[0] == 'mayor')
    assert(s.endswith('sus')[0] == 'jesus')
    assert(s.startswith('cre')[0] == 'crear')
