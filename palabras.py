# Biblioteca de funciones para trabajar con cadenas


def longitud(cadena: str) -> int:
    l = len(cadena)

    return l


def invertir(cadena: str) -> str:
    """
    Invierte una cadena.

    :param cadena: Cadena a evaluar.

    :return: Cadena invertida.
    """

    return cadena[::-1]

