# WordleCorpus

Proyecto basado en Wordle, consistente en una clase Corpus que puede cargar
un fichero de palabras, a raíz de una por línea, incluyendo la posibilidad
de recuperar las frecuencias si se incluyen en la fuente.

## Issues

* Hints.hint() no respeta el límite COUNT=200 ¿Por qué?
* ✅ Estaría bien que Play.guess() devolviera el historial en 
lugar de devolver solo el último resultado
* ✅ El 'ACERTÓ' debería ser a color blanco sobre rojo
* Mejorar el corpus en español (eliminando basura) y en catalán
o inglés (añadiendo frecuencias, si las encuentro. Hace falta una forma de limitar el corpus por frecuencia
en los casos en que sea posible (español), ya que muchas de
las palabras del corpus no son razonablemente válidas
* regex() no devuelve las palabras ordenadas alfabéticamente
* Ver diferencias regex(), candidates() y hint()
* ✅ Devolver las letras prohibidas (opcional)
* ✅ Comprobar qué pasa con el juego cuando la palabra es 'rajon'
y los sucesivos intentos: 
menta 00101
nariz 12100
barro 02111 - debería ser 02101, ya que no hay dos erres en rajon
raros 22120 - como antes, debe ser 22020
racor 22021 - debe ser 22020
(Respuesta: usaba dos procesos diferentes, uno en Hints, el bueno, y 
otro en Play, el malo. Se unifican usando solo el de Hints)
* Estudiar la estructura de Hints y Play para que compartan __tries, quizás baste con hacer la estructura pública.

## Sugerencias

* Tener todos los corpus guardados al iniciar
* Tenerlos en una base de datos en vez de en texto