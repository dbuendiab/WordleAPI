import re

from WordleAPI import Corpus


class HintsError(Exception):
    pass


class Hints(Corpus):
    """Carga un corpus (en español, inglés, catalán o custom) y permite obtener
    una colección de palabras que puedan usarse como ayuda para jugar al
    Wordle. El formato de la respuesta de Wordle se traduce como '01122'
    (por ejemplo), que significa: la primera letra no está en la palabra (0),
    las dos siguientes, sí, pero no en lugar correcto (1).
    Las dos últimas están bien (2).

    Tiene la particularidad de que cada nueva pista se busca sobre el corpus
    restringido por las anteriores. Si se quiere volver a empezar, debe usarse
    el método reset()

    Puede hacerse servir como ayuda para los juegos<br>
    Wordle en inglés: https://www.powerlanguage.co.uk/wordle/<br>
    Wordle en español: https://wordle.danielfrg.com/<br>
    Wordle en catalán: https://gelozp.com/games/wordle/<br>
    O en modo custom, como en https://hellowordl.net/, donde puede cambiarse el número de letras.

    Ejemplo:
    >> hints = Hints.ingles()
    >> hints.hint("glare", "20102")
    Hay 12 palabras candidatas
    ['gadge', 'gaffe', 'gagee', 'gaine', 'gaize', 'gambe', 'gange', 'gauge', 'gauze', 'gazee', 'genae', 'getae']
    """

    @property
    def tries(self):
        """Devuelve la lista de intentos [(word, test),...], donde
        'word' es la palabra propuesta y 'test' es el código de aciertos
        en formato 'nnnnn', donde n es 0, 1, o 2."""
        return self.__tries

    def reset(self):
        """Reinicia el sistema, borrando las apuestas previas"""
        self.__tries = []
        self.__lista = self.lista

    def hint(self, word, test):
        """Presenta en pantalla la lista de palabras que cumplen
        la condición representada por 'word0 y 'test' (ver hint_list)"""
        lista = self.hint_list(word, test)
        length = len(lista)
        if length == 1:
            print(lista)
        elif length == 0:
            print("No hay candidatas")
        else:
            lista = sorted(lista)
            print("Hay", length, "palabras candidatas")
            print(lista)

    def hint_list(self, word, test):
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
        except AttributeError:
            self.__tries = []
            self.__lista = self.lista  ## Viene de CorpusBase

        lista = None

        ## test = '22222' -> Éxito!
        if test == ("2" * self.word_size):  ## 22222, por defecto
            self.__tries.append((word, test))
            lista = [word]
            self.__lista = lista

        ## Añadir la apuesta a la lista de apuestas
        elif self.__validar_apuesta(word, test):
            self.__tries.append((word, test))
            lista = self.__lista

            ## Recorre las apuestas, reduciendo el corpus en cada iteración
            for (w, t) in self.__tries:
                if w:
                    lista = self.__reduce(lista, w, t)

            ## Guarda el corpus para la próxima vez
            self.__lista = lista

        else:
            raise HintsError("Error en la apuesta")

        ## Devuelve las palabras válidas tras la última iteración
        return lista

    @staticmethod
    def compare(target, guess):
        """Compara la palabra propuesta (guess) con la buscada (target)
        Devuelve la cadena de aciertos (p.ej. '22001')"""
        if len(target) != len(guess):
            raise HintsError("Las cadenas '{}' y '{}' tienen longitudes diferentes".format(target, guess))
        result = '0' * len(target)
        forbidden = set()
        i = 0
        while i < len(target):
            t = target[i]
            g = guess[i]
            # print(i, t, g)
            if t == g:
                result = result[:i] + '2' + result[i + 1:]
                target = target[:i] + ' ' + target[i + 1:]
            i += 1

        i = 0
        while i < len(guess):
            g = guess[i]
            r = result[i]
            if r != '2':
                if g in target:
                    result = result[:i] + '1' + result[i + 1:]
                    target = target.replace(g, ' ', 1)
                else:
                    result = result[:i] + '0' + result[i + 1:]
                    forbidden.add(g)
            i += 1

        return (result, forbidden)

    def __validar_apuesta(self, word, test):
        ## Comprueba que word y test tengan formatos correctos
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

    def __reduce(self, lista, word, test):
        ## Recorrer el corpus validándolo contra la salida de compare()
        nueva_lista = []
        for elem in lista:
            comparation, _ = Hints.compare(elem, word)
            if comparation == test:
                nueva_lista.append(elem)
        return nueva_lista
