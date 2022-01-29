from WordleAPI import Corpus
from WordleAPI import Search

# c = Corpus.ingles()
# print(c.pick())

# c = Corpus.ingles(word_size=8)
# print(c.pick())

# ##  print(c.lista)
# print("{} {} existe!".format("squailer", c.exists("squailer")))


def show_data_corpus(cp, palabra_sí, palabra_no):
    "Cargar distintos corpus"
    print("==============================================")
    print("Ver los parámetros del corpus")
    print("-----------------------------")
    print("Origen del corpus:", cp.origen)
    print("Líneas: {}, Palabras: {}, WordSize: {}".format(cp.num_lineas, cp.num_palabras, cp.word_size))
    print("Número de errores: {}".format(cp.num_errores))
    print()
    print("Muestreo: corpus.pick([num])")
    print("----------------------------")
    print("pick():", cp.pick())
    print("pick(10):", cp.pick(10))
    print("corpus (muestra):", cp.corpus[:10])
    print()
    print("Existencia corpus.exists(palabra)")
    print("---------------------------------")
    print("La palabra {} existe".format(palabra_sí))
    print("La palabra {} no existe".format(palabra_no))
    print()


def test1():
    "Cargar diferentes corpus"
    print("TEST 1\n======")
    print("Cargar corpus inglés por defecto (word_size=5)")
    cp = Corpus.ing()
    show_data_corpus(cp, "wound", "kaska")

    print("Cargar corpus español por defecto (word_size=5)")
    cp = Corpus.esp()
    show_data_corpus(cp, "corta", "crrta")

    print("Cargar corpus catalán por defecto (word_size=5)")
    cp = Corpus.cat()
    show_data_corpus(cp, "camio", "xscot")

    print("Cargar corpus inglés con word_size=8 (no default)")
    cp = Corpus.ing(word_size=8)
    show_data_corpus(cp, "exploder", "ppccppcc")

    print("Cargar corpus español con word_size=10 (no default)")
    cp = Corpus.esp(word_size=10)
    show_data_corpus(cp, "paradillas", "pprrdillas")

    print("Cargar corpus catalán con word_size=3 (no default)")
    cp = Corpus.cat(word_size=3)
    show_data_corpus(cp, "mar", "xxx")


def test2():
    "Pruebas con el método select() de corpuses.Corpus()"
    print("TEST 2\n======")
    print("Buscar palabras que empiezan por 'br'")
    cp = Search.esp()
    result = cp.search(lambda x: x[0].startswith('br') and x[1] > 1.0, tipo=1)
    print(result)


def test3():
    print("TEST 3\n======")
    print("Prueba de la clase Play")
    from WordleAPI import Play
    p = Play.esp()
    p.reset()
    p._Play__word = 'could'
    p._Play__count = 0
    p.guess('women')
    p.guess('gouts')
    p.guess('pouch')
    p.candidates()
    p.guess('courd')
    p.candidates()
    p.guess('could')
    p.candidates()


def test4():
    print("TEST 4\n======")
    print("Prueba de la clase Hints")
    from WordleAPI import Hints
    h = Hints.esp()
    lista = h.hint_list('menta', '00101')
    print(len(lista))


if __name__ == "__main__":
    ## test1()
    ## test2()
    test3()
    ## test4()
