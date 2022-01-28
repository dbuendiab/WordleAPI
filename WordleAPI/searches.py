import types
import re

from WordleAPI import Corpus


class Search(Corpus):
    """Una clase Search que especializa un Corpus para utilizarlo en búsquedas:

    from WordleAPI import Search

    s = Search.español(0)
    w = s.search(filtro_func=lambda x: x[0], orden_func=lambda x: x[1], reverse=True, count=50, tipo=1)
    w = s.regex("^..r.a$")
    w = s.startswith("ar", count=15)
    w = s.endswith('ido')
    """

    ## Número de palabras a devolver (por defecto)
    COUNT = 200

    def search(self, filtro_func=None, orden_func=None, reverse=None, count=None, tipo=0):
        """Obtiene un conjunto de palabras del corpus, posiblemente filtradas y ordenadas

        filtro_func: Si se incluye una función lambda x: patron.match(x[0]) (por ejemplo), limita las palabras según ese criterio
        orden_func: Si se especifica una función lambda x: x[0],usa esa ordenación
        reverse: True o False, funciona en combinación con el parámetro anterior, si existe
        count: Número de palabras a devolver. Por defecto, 100. El valor 0 las devuelve todas
        tipo: 0-Devolver la palabra; 1-Devolver la palabra acentuada (si hay); 2-Devolver la tupla completa"""

        ## Validación de parámetros: la función de filtro es obligatoria
        if filtro_func is None:
            print("Debe introducir alguna función de filtrado")
            return None
        elif not isinstance(filtro_func, types.FunctionType):
            print("filtro_func debe ser una función (lambda o def)", types.FunctionType, type(filtro_func))
            return None

        ## La función de ordenación no es obligatoria, pero debe ser función, si está
        if orden_func is not None:
            if not isinstance(orden_func, types.FunctionType):
                print("orden_func debe ser una función (lambda o def)")
                return None

        ## El parámetro reverse es opcional y, si está, booleano
        if reverse is None:
            reverse = False
        elif not isinstance(reverse, bool):
            print("Parámtro 'reverse' ha de ser True o False")
            return None

        ## La cuenta (número de resultados, si es > 0)
        if count is None:
            count = Search.COUNT
        elif not isinstance(count, int):
            count = Search.COUNT
        elif count <= 0:
            count = Search.COUNT    ## Default si no hay valor específico

        ## Formato de la salida
        if tipo not in (0, 1, 2):
            print("El tipo debe ser 0 (palabra solo), 1 (palabra acentuada, si existe), 2 (la tupla completa)")
            return None

        ## Filtrado del corpus (curioso: words es un objeto filter (no una lista))
        words = filter(filtro_func, self.corpus)

        ## Filtrado opcional del resultado
        if orden_func:
            words = sorted(words, key=orden_func, reverse=reverse)

        ## Convertir el generador <filter> a lista explícita
        words = [x for x in words]
        if count > 0:
            words = words[:count]

        ## Devolver las palabras o las palabras acentuadas o la tupla
        if tipo == 0:
            words = [x[0] for x in words]
        elif tipo == 1:
            words = [x[2] if len(x) == 3 else x[0] for x in words]

        return words

    def regex(self, regex, orden_func=None, reverse=None, count=None, tipo=0):
        patron = re.compile(regex)
        return self.search(lambda x: patron.match(x[0]), orden_func, reverse, count, tipo)

    def startswith(self, init_chars, orden_func=None, reverse=None, count=None, tipo=0):
        return self.search(lambda x: x[0].startswith(init_chars), orden_func, reverse, count, tipo)

    def endswith(self, end_chars, orden_func=None, reverse=None, count=None, tipo=0):
        return self.search(lambda x: x[0].endswith(end_chars), orden_func, reverse, count, tipo)

