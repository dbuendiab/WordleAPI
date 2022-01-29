from WordleAPI.corpus_read import CorpusBase
from WordleAPI import Corpus
from WordleAPI import Search
from WordleAPI import Hints
from WordleAPI import HintsError
import pytest


def test_init():
    "Comprobación funcionamiento instancia Hints"
    ## Instanciación
    h = Hints.español()
    assert(isinstance(h, Hints))
    assert(isinstance(h, Search))
    assert(isinstance(h, Corpus))
    assert(isinstance(h, CorpusBase))

    ## Método compare()
    assert(h.compare("rajon", "menta") == ('00101', {'e', 'm', 't'}))
    assert(h.compare("rajon", "nariz") == ('12100', {'i', 'z'}))
    assert(h.compare("rajon", "barro") == ('02101', {'b', 'r'}))
    assert(h.compare("rajon", "raros") == ('22020', {'r', 's'}))
    assert(h.compare("rajon", "racor") == ('22020', {'c', 'r'}))
    assert(h.compare("rajon", "rajon") == ('22222', set()))

    ## Errores en compare() si longitudes distintas
    with pytest.raises(HintsError):
        h.compare('pepe', 'antonio')
    with pytest.raises(HintsError):
        h.compare('antonio', 'pepe')

    ## Método hint()
    assert(len(h.hint_list('menta', '00101')) == 2035)
    assert(len(h.hint_list('nariz', '12100')) == 33)
    assert(len(h.hint_list('barro', '02101')) == 14)
    assert(len(h.hint_list('raros', '22020')) == 12)
    assert(len(h.hint_list('racor', '22020')) == 12)
    assert(len(h.hint_list('rajon', '22222')) == 1)
    assert(len(h.hint_list('menta', '00101')) == 1)
    assert(len(h.hint_list('eeeee', '00000')) == 1)

    ## Efecto de la acción de reset()
    h.reset()
    assert(len(h.hint_list('menta', '00101')) == 2035)
    assert(h.tries == [('menta', '00101')])
    h.hint_list('nariz', '12100')
    assert(h.tries == [('menta', '00101'), ('nariz', '12100')])
    h.hint_list('barro', '02101')
    assert(h.tries == [('menta', '00101'), ('nariz', '12100'), ('barro', '02101')])
    h.hint_list('raros', '22020')
    assert(h.tries == [('menta', '00101'), ('nariz', '12100'), ('barro', '02101'), ('raros', '22020')])
    h.hint_list('racor', '22020')
    assert(h.tries == [('menta', '00101'), ('nariz', '12100'), ('barro', '02101'), ('raros', '22020'),
    ('racor', '22020')])
    h.hint_list('rajon', '22222')
    assert(h.tries == [('menta', '00101'), ('nariz', '12100'), ('barro', '02101'), ('raros', '22020'),
    ('racor', '22020'), ('rajon', '22222')])

    ## Errores en compare() si longitudes distintas
    with pytest.raises(HintsError):
        h.hint('pepe', '0101000')
    with pytest.raises(HintsError):
        h.hint('antonio', '0212')
    with pytest.raises(HintsError):
        h.hint('antonio', '1232100')

