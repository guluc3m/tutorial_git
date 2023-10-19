import aritmetica as a
import palabras as p

def multiplicar(num1: int, num2: int) -> int:
    """Multiplica dos números enteros y devuelve el resultado"""
    # ¡Utiliza la función "sumar" de la biblioteca "aritmetica"!
    pass

def es_palindromo(palabra: str) -> bool:
    """Devuelve True si la palabra es un palíndromo, False si no lo es"""
    # ¡Utiliza la función "invertir" de la biblioteca "palabras"!
    pass
    
def main():
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
    print("Y si escribieras" , numero, "veces la palabra, escribirías",
          multiplicar(p.longitud(palabra), numero), "letras en total")
    pass

if __name__ == "__main__":
    main()
