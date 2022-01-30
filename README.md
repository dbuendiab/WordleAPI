# WordleCorpus

Proyecto basado en Wordle, consistente en una clase Corpus que puede cargar
un fichero de palabras, a raíz de una por línea, incluyendo la posibilidad
de recuperar las frecuencias si se incluyen en la fuente.

La jerarquía tiene dos ramas:

* CorpusBase -> Corpus -> Search
* CorpusBase -> Corpus -> Hints -> Play

Y hasta donde veo ahora, Play no necesita Search para nada.

## Issues

* Actualizar la documentación del código para contemplar los cambios de última hora
* Considerar un flag opcional de ayudas sí/no
* Mejorar los corpus en catalán o inglés (añadiendo frecuencias, si las encuentro)

## Sugerencias

* Tener todos los corpus guardados al iniciar
* Tenerlos en una base de datos en vez de en texto

## Issues cerrados

* ✅Cambiado el corpus en español por un subconjunto de palabras de +3 letras y frecuencia > 0.5. Salen algo más de 60.000.
* ✅Cambiar los print() en Hints.hint
* ✅Hints.hint() no respeta el límite COUNT=200 ¿Por qué? (Porque Hints.hint() no usa Search.search())
* ✅forbidden (Play) no se acumulan entre tiradas
* ✅Reparar hint() en Play.candidates()
* ✅Estudiar la estructura de Hints y Play para que compartan __tries, quizás baste con hacer la estructura pública.
* ✅Cambiar los nombres de los method class: español -> spa, ingles -> ing, catalan -> cat (con todo el lío asociado)
* ✅Estaría bien que Play.guess() devolviera el historial en lugar de devolver solo el último resultado
* ✅El 'ACERTÓ' debería ser a color blanco sobre rojo
* ✅regex() no devuelve las palabras ordenadas alfabéticamente
* ✅Ver diferencias regex(), candidates() y hint()
* ✅Devolver las letras prohibidas (opcional)
* ✅Comprobar qué pasa con el juego cuando la palabra es 'rajon' y los sucesivos intentos: 

    menta 00101

    nariz 12100

    barro 02111 - debería ser 02101, ya que no hay dos erres en rajon

    raros 22120 - como antes, debe ser 22020

    racor 22021 - debe ser 22020

    (Respuesta: usaba dos procesos diferentes, uno en Hints, el bueno, y otro en Play, el malo. Se unifican usando solo el de Hints)
