"""
Módulo para la generación de números aleatorios usando el algoritmo LGC.

Autor: Pere [Afegeix els teus cognoms]
Descripción: Este módulo implementa un generador lineal congruente (LGC) 
mediante una clase iterable (Aleat) y una función generadora (aleat).
"""

class Aleat:
    """
    Clase iterable que implementa un generador de números aleatorios LGC.
    
    Atributos:
        m (int): Módulo.
        a (int): Multiplicador.
        c (int): Incremento.
        xn (int): Valor actual de la secuencia (semilla).
        
    Pruebas unitarias (Comprobación del funcionamiento):
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15
    
    Pruebas unitarias (Comprobación del reinicio):
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """
    
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.xn = x0

    def __iter__(self):
        return self

    def __next__(self):
        # Aplicamos la fórmula LGC
        self.xn = (self.a * self.xn + self.c) % self.m
        return self.xn

    def __call__(self, x0):
        # Reinicia la secuencia con una nueva semilla
        self.xn = x0


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora que implementa un generador de números aleatorios LGC.
    
    Argumentos (por clave):
        m (int): Módulo.
        a (int): Multiplicador.
        c (int): Incremento.
        x0 (int): Semilla inicial.
        
    Salida:
        Iterador que produce números pseudoaleatorios. En caso de recibir un 
        valor mediante el método send(), reinicia la secuencia usando ese valor.
        
    Pruebas unitarias (Comprobación del funcionamiento):
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44
    
    Pruebas unitarias (Comprobación del reinicio):
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    xn = x0
    while True:
        xn = (a * xn + c) % m
        # yield devuelve el valor generado y captura lo que llegue por send()
        nueva_semilla = yield xn 
        if nueva_semilla is not None:
            xn = nueva_semilla


if __name__ == "__main__":
    import doctest
    doctest.testmod()