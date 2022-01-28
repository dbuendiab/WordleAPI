import re

from WordleAPI import Search


class HintsError(Exception):
    pass


class Hints(Search):
    """Carga un corpus (en español, inglés, catalán o custom) y permite obtener
    una colección de palabras que puedan usarse como ayuda para jugar al
    Wordle. El formato de la respuesta de Wordle se traduce como '01122'
    (por ejemplo), que significa: la primera letra no está en la palabra (0),
    las dos siguientes, sí, pero no en lugar correcto (1).
    Las dos últimas están bien (2).

    Tiene la particularidad de que cada nueva pista se busca sobre el corpus
    restringido por las anteriores. Si se quiere volver a empezar, debe usarse
    el método reset()

    Puede hacerse servir como ayuda para los juegos
    Wordle en inglés: https://www.powerlanguage.co.uk/wordle/
    Wordle en español: https://wordle.danielfrg.com/
    Wordle en catalán: https://gelozp.com/games/wordle/
    O en modo custom, como en https://hellowordl.net/, donde puede cambiarse el número de letras.

    Ejemplo:
    >> hints = Hints.ingles()
    >> hints.hint("glare", "20102")
    Hay 12 palabras candidatas
    ['gadge', 'gaffe', 'gagee', 'gaine', 'gaize', 'gambe', 'gange', 'gauge', 'gauze', 'gazee', 'genae', 'getae']
    """

    # def __init__(self, idioma=None, corpus=None):
    #     """Creación del corpus de soporte
    #     Parámetros:
    #     idioma: Opcional. Debe ser español, ingles o catalan
    #     corpus: Opcional. Un corpus creado previamente, customizado a medida.
    #     Debe introducirse uno solo de los dos.
    #     """
    #     ## Definir el corpus fuera de los condicionales
    #     self.__corpus = None

    #     if idioma == None and corpus == None:
    #         raise HintsError("Debe introducir parámetro idioma ó un corpus")
    #     elif idioma != None:
    #         if idioma not in ("ingles", "español", "catalan"):
    #             raise HintsError("Los idiomas válidos son 'español', 'ingles', 'catalan'")
    #         elif idioma == "ingles":
    #             self.__corpus = CorpusAPI.Corpus.ingles()
    #         elif idioma == "español":
    #             self.__corpus = CorpusAPI.Corpus.español()
    #         elif idioma == "catalan":
    #             self.__corpus = CorpusAPI.Corpus.catalan()
    #     else:
    #         if isinstance(corpus, CorpusAPI.Corpus):
    #             self.__corpus = corpus
    #         else:
    #             raise HintsError("No ha introducido un objeto Corpus")
    #     self.reset()

    def reset(self):
        """Reinicia el sistema, borrando las apuestas previas"""
        self.__tries = []
        self.__lista = self.lista

    # @staticmethod
    # def __set_invalid_chars(word, test):
    #     invalid_chars = set()
    #     needed_chars = set()
    #     set_chars = set()
    #     for (c, p) in zip(word, test):
    #         if p == '0':
    #             invalid_chars.add(c)
    #         if p == '1':
    #             needed_chars.add(c)
    #         if p == '2':
    #             set_chars.add(c)
    #     # print("invalid, needed, set (1): ", invalid_chars, needed_chars, set_chars)
    #     invalid_chars = invalid_chars - set_chars
    #     invalid_chars = invalid_chars - needed_chars
    #     # print("invalid, needed, set (2): ", invalid_chars, needed_chars, set_chars)
    #     return (invalid_chars, needed_chars)

    @staticmethod
    def __compare(target, guess):
        result = ''
        i = 0
        while i < len(target):
            t = target[i]
            g = guess[i]
            # print(i, t, g)
            if t == g:
                result += '2'
                target = target[:i] + ' ' + target[i + 1:]
            else:
                if g in target:
                    result += '1'
                    target = target.replace(g, ' ', 1)
                else:
                    result += '0'
            i += 1
        return result

    def __reduce(self, lista, word, test):
        ## Recorrer el corpus validándolo contra la salida de compare()
        nueva_lista = []
        for elem in lista:
            if Hints.__compare(elem, word) == test:
                nueva_lista.append(elem)
        return nueva_lista

    def __validar_apuesta(self, word, test):
        if len(word) != self.word_size:
            print("La palabra debe tener {} caracteres".format(self.word_size))
            return False
        if len(test) != self.word_size:
            print("El test debe tener {} caracteres (0, 1 y 2)".format(self.word_size))
            return False
        patron = "[012]{%d}" % self.word_size
        if not re.match(patron, test):
            print("El test usa solo: 0-letra no está; 1-letra está, pero no en su sitio; 2-letra está en su sitio")
            return False
        return True

    def hint(self, word, test, verbose=True):
        """Devuelve una colección de palabras que cumplen con el criterio descrito por 'test'.
        Construye un corpus nuevo limitado a esa colección, para usarlo en la siguiente iteración.
        Parámetros:
        word: La última palabra introducida en Wordle
        test: El código de colores que devuelve Wordle:
            0: letra no está, 1: está pero mal puesta, 2: la letra está en su lugar.
        """
        ## Tengo el problema de inicializar tries sin perder los classmethods de Corpus ni reescribirlos
        try:
            _ = self.__tries
        except:
            self.__tries = []
            self.__lista = self.lista

        ## test = '22222' -> Éxito!
        if test == "2" * self.word_size:  ## 22222, por defecto
            print("Acertó!!!")
            return

        ## Añadir la apuesta a la lista de apuestas
        if self.__validar_apuesta(word, test):
            self.__tries.append((word, test))
            lista = self.__lista

            ## Recorre las apuestas, reduciendo el corpus en cada iteración
            for t in self.__tries:
                if t[0]:
                    lista = self.__reduce(lista, t[0], t[1])

            ## Guarda el corpus para la próxima vez
            self.__lista = lista

            ## Muestra las palabras válidas tras la última iteración
            lista = sorted(lista)
            if verbose is True:
                print("Hay", len(lista), "palabras candidatas")
                print(lista)
            else:
                return lista
                

        else:
            raise HintsError("Error en la apuesta")
