# Repositorio de ejercicios para la charla "Introducción a Git y GitHub"

En este repositorio encontraréis ejercicios muy sencillos de programación en Python, pensados para ser hechos en equipos de dos personas, para aprender los fundamentos de Git, GitHub, y el _pair programming_.


## Pasos a seguir
1. Haced un _fork_ de éste repositorio (sólo uno del equipo).
2. Añadid como colaborador del _fork_ al otro compañero del equipo (`Settings` → `Collaborators and teams` → `Add people`).
3. Clonad el repositorio (ambas personas).
4. Uno de los miembros rellenará las funciones del archivo [`aritmetica.py`](aritmetica.py) y el otro rellenará las de [`palabras.py`](palabras.py).
5. Cada uno hará un _commit_ y un _push_. Observad cómo no hay conflictos debido a trabajar en distintos archivos.
6. Se refrescarán los cambios mediante un _pull_.
7. Cread dos ramas nuevas: `funciones` y `algo`, para poder trabajar en el mismo archivo sin problemas.
8. Uno hará un _checkout_ a la rama `funciones` y el otro a la rama `algo`.
9. El de la rama `funciones` se encargará de rellenar las funciones `multiplicar()` y `es_palindromo()`, mientras que el de la rama `algo` se encargará de la función `haz_algo_con()`.
10. Haced _commit_ y _push_ a vuestras respectivas ramas.
11. Haced una _pull request_ de la rama `funciones` a la rama `main`. Observad cómo no hay conflictos. Eliminad la rama `funciones`.
11. Haced una _pull request_ de la rama `algo` a la rama `main`. Resolved los conflictos y eliminad la rama `algo`.
12. Haced una _pull request_ al repositorio original. La mejor _pull request_ de entre todos los asistentes será la aceptada.


## Instalación y ejecución
Asegúrate de tener Python3 instalado.
```bash
python3 main.py
```

