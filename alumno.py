class Alumno:
    """
    Clase usada para el tratamiento de las notas de los alumnos. Cada uno
    incluye los atributos siguientes:

    numIden:   Número de identificación. Es un número entero que, en caso
               de no indicarse, toma el valor por defecto 'numIden=-1'.
    nombre:    Nombre completo del alumno.
    notas:     Lista de números reales con las distintas notas de cada alumno.
    """

    def __init__(self, nombre, numIden=-1, notas=[]):
        self.numIden = numIden
        self.nombre = nombre
        self.notas = [nota for nota in notas]

    def __add__(self, other):
        """
        Devuelve un nuevo objeto 'Alumno' con una lista de notas ampliada con
        el valor pasado como argumento. De este modo, añadir una nota a un
        Alumno se realiza con la orden 'alumno += nota'.
        """
        return Alumno(self.nombre, self.numIden, self.notas + [other])

    def media(self):
        """
        Devuelve la nota media del alumno.
        """
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def __repr__(self):
        """
        Devuelve la representación 'oficial' del alumno. A partir de copia
        y pega de la cadena obtenida es posible crear un nuevo Alumno idéntico.
        """
        return f'Alumno("{self.nombre}", {self.numIden!r}, {self.notas!r})'

    def __str__(self):
        """
        Devuelve la representación 'bonita' del alumno. Visualiza en tres
        columnas separas por tabulador el número de identificación, el nombre
        completo y la nota media del alumno con un decimal.
        """
        return f'{self.numIden}\t{self.nombre}\t{self.media():.1f}'

import re

def leeAlumnos(ficAlumnos):
    '''
    Con esta funcion leemos el fichero de texto alumnos.txt y extraemos
    un diccionario con los datos de los alumnos que hay dentro del documento.

    >>> alumnos = leeAlumnos('alumnos.txt')
    >>> for alumno in alumnos:
    ...     print(alumnos[alumno])
    ...
    171     Blanca Agirrebarrenetse 9.5
    23      Carles Balcells de Lara 4.9
    68      David Garcia Fuster     7.0
    '''
    expr_id = r"(?P<id>\d+)\s+"
    expr_nom = r"(?P<nom>[\w\s]+?)\s+"
    expr_notes = r"(?P<notes>[\d.]+)\s"
    # Expresión regular para leer el fichero de alumnos
    # \s* : Espacio en blanco opcional
    # (?P<id>\d+) : Grupo con nombre id que contiene uno o más dígitos
    # (?P<nom>[\w\s]+?) : Grupo con nombre nom que contiene uno o más caracteres alfanuméricos o espacios
    # (?P<notes>[\d.]+) : Grupo con nombre notes que contiene uno o más dígitos o puntos
    # \s : Espacio en blanco
    # \s* : Espacio en blanco opcional

    expresion = re.compile(expr_id + expr_nom + expr_notes) #r: regular s: space d: digit + es una o mas veces, *
    students = {}

    with open(ficAlumnos, 'rt') as fpAlumnos:
        for linea in fpAlumnos:
            match = expresion.search(linea)
            if match is not None:
                name = match['nom']
                id = int(match['id'])
                marks = [float(mark) for mark in match['notes'].split()]
                students[name] = Alumno(name,id,marks)
    return students

print(leeAlumnos('alumnos.txt'))

if __name__ == "__main__":
      import doctest
      doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)