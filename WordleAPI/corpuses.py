from WordleAPI import CorpusBase

ruta_ingles = r"txt\words_alpha.txt"
ruta_español = r"txt\CREA_total.TXT"
ruta_catalan = r"txt\paraules_cat.txt"


class Corpus(CorpusBase):
    """Devuelve los corpus de los idiomas predeterminados disponibles"""

    @classmethod
    def ing(cls, word_size=5):
        """Corpus predeterminado en inglés"""
        return cls(ruta_ingles, word_size=word_size)

    @classmethod
    def esp(cls, word_size=5):
        """Corpus predeterminado en español"""
        patron1 = r".+\t(\w+).+"
        patron2 = r".+\t.+\t\s*(\d+\.\d+)"
        acentos = (('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u'), ('ü', 'u'))
        ignore_lines = 1
        return cls(ruta_español, pattern=patron1, word_size=word_size, pattern_freq=patron2, list_char_conversion=acentos, ignore_lines=ignore_lines)

    @classmethod
    def cat(cls, word_size=5):
        "Corpus predeterminado en catalán"
        return cls(ruta_catalan, word_size=word_size)
