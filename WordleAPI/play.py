import random
from WordleAPI import Hints
from WordleAPI import output


class PlayError(Exception):
    pass


class Play(Hints):
    """Inicia un juego Wordle local

    Al iniciar la clase, se crea una palabra aleatoria que hay que acertar.

    Ejemplo:
    --------
    >> from WordleAPI import Play
    >> juego = Play.ingles()


    >> palabra = "afars"
    >> acierto = juego.guess(palabra)
    >> if acierto != True:
    ..     juego.hint(palabra, acierto)

    Ejemplo custom:
    ---------------
    >> wC = CorpusAPI.Corpus("words_alpha.txt", word_size=6)
    >> wC.word_size
    6
    >> wP = WordlePlay(corpus=wC)
    >> wW = WordleTest(corpus=wC)
    >> wW.hint("bowler", "011001")
    (bowler, 011001) --> regex: /.[^o][^w]..[^r]/ - invalid: {'b', 'l', 'e'} - needed: {'o', 'w', 'r'}
    Hay 54 palabras candidatas
    ['afrown', 'arrows', 'arrowy', 'avowry', 'aworry', 'aworth', 'awrong', 'carrow', 'chowry', 'crakow',
    'crowds', 'crowdy', 'crowns', 'drownd', 'drowns', 'drowsy', 'farrow', 'frowns', 'frowny', 'frowst',
    'frowsy', 'frowzy', 'furrow', 'growan', 'growth', 'harrow', 'ingrow', 'iworth', 'marrow', 'narrow',
    'outrow', 'rwound', 'sarrow', 'strowd', 'strown', 'strows', 'swords', 'tarrow', 'thrown', 'throws',
    'trowth', 'ungrow', 'upgrow', 'vrouws', 'warori', 'warrok', 'whorry', 'whorts', 'winrow', 'wrocht',
    'wrongs', 'wrothy', 'wyrock', 'yarrow']
    """

    def reset(self):
        'Inicia juego nuevo'
        self.__word = self.pick()[0]
        # self.__last_word = None
        # self.__last_test = None
        self.__count = 0
        self.__tries = []
        self.__forbidden = set()
        super().reset()   ## Los hints se actualizarán automáticamente con guess()

    @property
    def the_word(self):
        return self.__word

    def candidates(self, num=0):
        """Devuelve la lista de hints para el juego actual
        Los hints se recalculan cada vez que se prueba un intento
        mediante guess()"""
        if num <= 0:
            return self.__hints
            # return self.hint(self.__last_word, self.__last_test)
        else:
            return random.salple(self.__hints, num)
            # return random.sample(self.hint(self.__last_word, self.__last_test), num)

    def guess(self, word):
        try:
            _ = self.__word
        except:
            self.reset()
            output.aviso("JUEGO REINICIADO")

        if self.exists(word) is False:
            output.aviso2("Esa palabra no existe")
            return None

        self.__count += 1
        output.aviso2("Intento: {}".format(self.__count))

        if self.__word == word:
            output.aviso("ACERTÓ!!!")
            output.printc(word, "2" * len(word), last=True)
            return True

        test = ""
        for (c1, c2) in zip(word, self.__word):
            if c1 == c2:
                test += "2"
            else:
                if c1 in self.__word:
                    test += "1"
                else:
                    test += "0"
                    self.__forbidden.add(c1)

        self.__hints = self.hint(word, test, verbose=False)

        self.__tries.append((word, test))

        output.aviso2(''.join(sorted(list(self.__forbidden))))
        for (w, t) in self.__tries[:-1]:
            output.printc(w, t)
        output.printc(word, test, last=True)
        #output.printc(word, test)
        # self.__last_word = word
        # self.__last_test = test
        return test
