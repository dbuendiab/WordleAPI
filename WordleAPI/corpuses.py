import os.path
from WordleAPI import CorpusBase

ruta_ing = os.path.join("txt", "words_alpha.txt")
ruta_esp = os.path.join("txt", "palabra2.txt")
ruta_cat = os.path.join("txt", "paraules_cat.txt")


class Corpus(CorpusBase):
    """Devuelve los corpus de los idiomas predeterminados disponibles"""

    @classmethod
    def ing(cls, word_size=5):
        """Corpus predeterminado en inglés"""
        return cls(ruta_ing, word_size=word_size)

    @classmethod
    def esp(cls, word_size=5):
        """Corpus predeterminado en español"""
        ## patron1 = r".+\t(\w+).+"
        patron1 = r"(\w+).+"
        ## patron2 = r".+\t.+\t\s*(\d+\.\d+)"
        patron2 = r".+\s(\d+\.\d+)"
        acentos = (('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u'), ('ü', 'u'))
        #ignore_lines = 1
        ignore_lines = 0
        return cls(ruta_esp, pattern=patron1, word_size=word_size, pattern_freq=patron2, list_char_conversion=acentos, ignore_lines=ignore_lines)

    @classmethod
    def cat(cls, word_size=5):
        "Corpus predeterminado en catalán"
        return cls(ruta_cat, word_size=word_size)
