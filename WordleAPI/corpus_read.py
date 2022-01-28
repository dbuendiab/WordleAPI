import codecs
import re
## import WordleAPI


class CorpusBase:

    def __init__(self, textfile, pattern=None, word_size=5, pattern_freq=None, list_char_conversion=[], ignore_lines=0):
        """Recupera las palabras de un fichero externo
        El formato debe ser de línea por palabra, pero puede incluir un campo de frecuencia para ordenación

        Parámetros:
        textfile: el nombre del fichero de texto
        pattern: patrón regex para localizar la palabra dentro de la línea
        word_size: tamaño de las palabras seleccionadas (<1: todas)
        pattern_freq: patrón regex para el campo numérico que regirá la ordenación
        list_char_conversion: lista de duplas con los caracteres que se sustituirán (acentos)
        ignore_lines: líneas de cabecera que se ignorarán

        Patrón CREA (palabras): r".+\t(\w+).+"
        Patrón CREA (frecuencias): r".+\t.+\t\s*(\d+).+"
        """
        ## Cargar el fichero
        texto = codecs.open(textfile, 'r', 'utf8').read()

        ## Fijar los patrones
        patron = None
        if pattern and isinstance(pattern, str):
            patron = re.compile(pattern)

        patron_frec = None
        if pattern_freq and isinstance(pattern_freq, str):
            patron_frec = re.compile(pattern_freq)

        ## Separador de líneas: uno de los dos normales
        separador = '\r\n' if '\r\n' in texto else '\n'

        ## Cargar las palabras
        corpus = list()
        num_lineas = 0
        num_palabras = 0
        errores = []

        for linea in texto.split(separador):

            ## Salta líneas de cabecera no válidas
            if ignore_lines > 0:
                ignore_lines -= 1
                continue

            num_lineas += 1
            if linea == '':
                continue

            ## La palabra, con patrón o toda la línea
            word = None
            if patron:
                m = patron.match(linea)
                if m:
                    word = m.groups(0)[0]
                    num_palabras += 1
                else:
                    errores.append(linea)
                    continue
            else:
                word = linea
                num_palabras += 1

            ## La frecuencia, si existe. Key y reverse es para futuras ordenaciones
            frecuencia = 1
            if patron_frec:
                m = patron_frec.match(linea)
                if m:
                    frecuencia = float(m.groups(0)[0])

            ## El filtro por tamaño, si hay
            if len(word) == word_size or word_size <= 0:

                ## Sustituir caracteres si es preciso
                new_word = word
                if list_char_conversion:
                    new_word = word
                    for (v1, v2) in list_char_conversion:
                        new_word = new_word.replace(v1, v2)

                ## Y ya por fin guardar
                if word != new_word:
                    corpus.append((new_word, frecuencia, word))
                else:
                    corpus.append((new_word, frecuencia))

        ## Guardar la instancia
        self.__corpus = tuple(corpus)
        self.__lista = tuple([x[0] for x in self.__corpus])
        self.__word_size = word_size if word_size > 0 else -1
        self.__palabras = num_palabras
        self.__lineas = num_lineas
        self.__file = textfile
        self.__errores = errores

    @property
    def origen(self):
        """Fichero de palabras"""
        return self.__file

    @property
    def num_lineas(self):
        "Número de líneas útiles en el fichero origen"
        return self.__lineas

    @property
    def num_palabras(self):
        "Número de palabras en el fichero origen"
        return self.__palabras

    @property
    def corpus(self):
        """Devuelve una lista de duplas (word, freq, [word_accent])"""
        return self.__corpus

    @property
    def lista(self):
        "Devuelve una lista de palabras (sin acentos) del corpus"
        return self.__lista

    @property
    def word_size(self):
        """Tamaño de las palabras (5 por defecto)"""
        return self.__word_size

    @property
    def num_errores(self):
        """Devuelve el número de líneas que no se pudieron decodificar"""
        return len(self.__errores)

    @property
    def errores(self):
        """Devuelve la lista de líneas no decodificadas que no se pudieron decodificar"""
        return self.__errores

    def exists(self, word):
        """Devuelve True si la palabra existe en el corpus"""
        return word in self.lista

    def pick(self, num_muestras=1):
        """Devuelve una o 'num_muestras' palabras aleatorias del corpus"""
        import random
        return random.sample(self.__lista, num_muestras)

    def find(self, word):
        """Devuelve la o las tuplas que corresponden a la palabra dada,
        incluyendo las tuplas con acentos (probar con 'había')"""
        return {x for x in self.__corpus if (x[0] == word) or (word == (x[2] if len(x) == 3 else x[0]))}
