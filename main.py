from typing import Any

import aritmetica as a
import palabras as p



def multiplicar(num1: int, num2: int) -> int:
    """
    Multiplica dos números enteros.

    :param num1: Número 1.
    :param num2: Número 2.

    :return: Producto de número 1 y número 2.
    """

    # ¡Utiliza la función "sumar" de la biblioteca "aritmetica"!
    ret = 0
    for i in range(num1):
        ret = ret + a.sumar(1, num2)
    return ret - num1


def es_palindromo(palabra: str) -> bool:
    """
    Evalua si una palabra es un palíndromo.

    :param palabra: Palabra a evaluar.

    :return: `True` si la palabra es un palíndromo, `False` en caso contrario.
    """

    # ¡Utiliza la función "invertir" de la biblioteca "palabras"!
    return (palabra == p.invertir(palabra))


def haz_algo_con(esto: str) -> Any:
    """
    Sé libre, haz algo con esto.

    :param esto: Algo.

    :return: ???
    """

    # ¡Tu código va aquí!
    print(esto + p.invertir(esto))
    return None



if __name__ == "__main__":

    palabra = input("Introduce una palabra: ")
    while palabra == "":
        palabra = input("Error.\nIntroduce una palabra: ")

    while True:
        try:
            numero = int(input("Introduce un número: "))
            break
        except ValueError:
            print("Error.")

    print("La palabra tiene", p.longitud(palabra), "letras")

    if es_palindromo(palabra):
        print("La palabra es un palíndromo")

    print("La palabra invertida es", p.invertir(palabra))

    print("Y si escribieras", numero, "veces la palabra, escribirías", multiplicar(p.longitud(palabra), numero), "letras en total")

    print("Y ahora, como gran final...")

    haz_algo_con("esto")

