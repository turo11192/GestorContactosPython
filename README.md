# GestorContactosPython
Gestor de contactos por consola con python (Un CRUD pero de manera más rudimentaria)

PROBLEMA: 

-----Ejercicio Final Módulo 1: Gestor de Contactos-----

*Descripción:
    Vamos a crear un gestor de contactos en consola que permita realizar varias acciones. El gestor debe permitir agregar, editar, eliminar y mostrar contactos. Cada contacto tendrá los siguientes atributos:

    Nombre

    Teléfono

    Correo electrónico

    Dirección

    También, se debe manejar un archivo donde se guardarán los contactos (para simular persistencia de datos). El archivo debe contener todos los contactos guardados en formato de texto (puedes elegir cómo almacenarlos, por ejemplo, JSON o CSV).

*Requisitos:
-Agregar un nuevo contacto:

    El programa debe pedir los datos del contacto (nombre, teléfono, correo electrónico y dirección).

    Si el contacto ya existe (por nombre), el sistema debe mostrar un mensaje de error y no agregarlo.

    Después de agregar el contacto, el sistema debe guardar los cambios en el archivo.

-Editar un contacto:

    El usuario puede elegir un contacto existente por nombre y editar uno o más campos.

    Los cambios deben guardarse en el archivo después de editar el contacto.

-Eliminar un contacto:

    El usuario puede eliminar un contacto por nombre.

    El contacto debe eliminarse del archivo también.

-Ver todos los contactos:

    El programa debe mostrar todos los contactos guardados en el archivo.

    Cada contacto debe mostrarse en formato legible.

-Validación de datos:

    El programa debe validar que el número de teléfono sea válido (puedes usar una expresión regular).

    El correo electrónico debe tener un formato válido.

    El programa debe manejar las excepciones adecuadamente (por ejemplo, si no se puede leer el archivo, si hay un error en los datos ingresados).

-Persistencia de datos:

    Los contactos deben guardarse en un archivo que persista entre ejecuciones del programa (puedes utilizar el formato .txt, .csv o .json).

-Manejo de excepciones:

    Usa excepciones para manejar los errores más comunes (por ejemplo, archivo no encontrado, errores de formato en los datos, etc.).


*Puntos adicionales:
-Extra: Puedes crear una opción de búsqueda de contacto por nombre o por número de teléfono.

-Extra: Puedes agregar una opción para ordenar los contactos por nombre.


*****Instrucciones*****
-Implemente el código de la clase Contacto y la clase GestorContactos.

-Implementa un sistema de menús para interactuar con el gestor de contactos.

-Asegúrate de manejar las excepciones adecuadamente (por ejemplo, si el archivo no existe al intentar cargar los contactos).

-Usa un archivo .json para guardar los contactos.

-Valida que los datos del teléfono y el correo electrónico sean correctos.

*****Evaluación*****
-¿Puedo agregar, editar y eliminar contactos?

-¿El programa guarda los cambios en el archivo correctamente?

-¿El manejo de excepciones funciona adecuadamente?

-¿El formato de los datos es correcto?

-¿El menú de opciones es fácil de usar y muestra los resultados esperados?
