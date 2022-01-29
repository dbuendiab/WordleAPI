import random
from WordleAPI import Hints
from WordleAPI import output


class PlayError(Exception):
    pass


## TODO Modificar los ejemplos con el comportamiento actualizado
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
        self.__candidates = []
        super().reset()   ## Los hints se actualizarán automáticamente con guess()

    @property
    def the_word(self):
        return self.__word

    ## TODO Reparar candidates -> hint()
    def candidates(self, num=0):
        """Devuelve la lista de hints para el juego actual
        Los hints se recalculan cada vez que se prueba un intento
        mediante guess()"""

        words = self.__candidates
        if len(words) > 30:
            words = random.sample(self.__candidates, 30)
        words = sorted(words)
        output.candidatas(', '.join(words))

    def guess(self, word):
        try:
            _ = self.__word
        except AttributeError:
            self.reset()
            print()
            output.aviso("          JUEGO REINICIADO            ")

        if self.exists(word) is False:
            output.aviso2("Esa palabra no existe")
            return

        self.__count += 1
        print()
        output.aviso2("Intento: {}".format(self.__count))

        if self.__word == word:
            output.aviso2("¡Correcto!")
            output.printc(word, "2" * len(word), last=True)
            self.__candidates = [word]
            return

        ## Uso la función compare de Hints para obtener el test
        test, forbidden = Hints.compare(self.__word, word)

        ## Pero el tries de Hints no me vale aquí, uso uno propio de Play
        self.__tries.append((word, test))
        self.__candidates = self.hint_list(word, test)

        ## Hay que añadir las nuevas letras descartadas a las anteriores
        self.__forbidden = self.__forbidden.union(forbidden)

        ## Presentación de los datos
        forbidden_string = ' '.join(sorted(list(self.__forbidden))).upper()
        output.forbidden(forbidden_string)

        for (w, t) in self.__tries:
            output.printc(w, t)
        ## output.printc(word, test, last=True)
