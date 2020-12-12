from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def leer_archivo(nombre):
    """
    Leer contenido de un archivo.
    :param str nombre: Nombre del archivo ("nombre.txt").
    :return: list[string]
    """
    nombre = "../recursor/archivos_quizmaker/"+nombre
    archivo = open(nombre,'r')
    lista_preguntas = archivo.readlines()
    return lista_preguntas

def obtener_dato(lista_preguntas, renglon, dato):
    """
    Obtiene el dato de una pregunta de una lista.
    :param list[string] lista_preguntas: Lista de preguntas.
    :param int renglon: Elemento de la lista de preguntas o línea.
    :param int dato: Dato a obtener de la pregunta (1 a 7).  
    :return: str
    """
    cadena = lista_preguntas[renglon] # Cadena 
    dato -= 1 # Actulización de dato
    dato_solicitado = cadena.split("^") # Lista con datos
    if dato == 6:
        return dato_solicitado[dato][:len(dato_solicitado[dato])-1]
    return dato_solicitado[dato]

def eliminar_pregunta(categ, posicion):
    """
    Elimina la pregunta de una posición o renglon en el archivo.
    :param str categ: Categoría larga de la pregunta (química, física, ...).
    :param str posicion: Posición de la pregunta a eliminar (pos > 1).
    """
    lista_preguntas = [] # Lista de preguntas a ser almacenada en archivo.
    categ = categ[len(categ)-3:len(categ)-1] # Categoría corta.
    vacio = False # Bandera para saber si un archivo está vacío

    if categ == "CM":
        vacio = is_archivo_vacio("Ciencias.txt")
        lista_preguntas = leer_archivo("Ciencias.txt")
    elif categ == "SC":
        vacio = is_archivo_vacio("Sociales.txt")
        lista_preguntas = leer_archivo("Sociales.txt")
    elif categ == "CT":
        vacio = is_archivo_vacio("Cultura.txt")
        lista_preguntas = leer_archivo("Cultura.txt")
    else:
        vacio = is_archivo_vacio("Entretenimiento.txt")
        lista_preguntas = leer_archivo("Entretenimiento.txt")

    if len(lista_preguntas) == 0:
        return

    if not(is_lista_vacio([posicion])):
        try:
            if int(posicion) <= len(lista_preguntas) and int(posicion) > 0:
                if vacio:
                    messagebox.showerror("Error","El archivo está vacío")
                else:
                    borrar_contenido_archivo(categ)
                    lista_preguntas.pop(int(posicion)-1)
                    guardar_lista_archivo(categ, lista_preguntas)
                    messagebox.showinfo("Eliminado correcto","La pregunta ha sido eliminada exitosamente")
            else:
                messagebox.showerror("Error", "Elija un número entre 1 y "+str(len(lista_preguntas)))
        except:
            messagebox.showerror("Error", "Ingrese un número")
    else:
        messagebox.showerror("Error", "Verifique que no hayan espacios en blanco")

def borrar_contenido_archivo(categ):
    """
    Borra todo el contenido de un archivo.
    :param str categ: Categoría corta del archivo para borrar el contenido (CM, SC, ...).
    """
    if categ == "CM":
        archivo = open("../recursor/archivos_quizmaker/Ciencias.txt", "w")
    elif categ == "SC":
        archivo = open("../recursor/archivos_quizmaker/Sociales.txt", "w")
    elif categ  == "CT":
        archivo = open("../recursor/archivos_quizmaker/Cultura.txt", "w")
    else:
        archivo = open("../recursor/archivos_quizmaker/Entretenimiento.txt", "w")

    archivo.close()

def guardar_lista_archivo(categ, lista_preguntas):
    """
    Guarda el contenido de una lista en el archivo.
    :param str categ: Categoría corta del archivo a guardar el contenido de la lista (CM, SC, ...).
    :param list[string] lista_preguntas: Lista de preguntas para ser almacenadas.
    """
    if categ == "CM":
        archivo = open("../recursor/archivos_quizmaker/Ciencias.txt", "a")
    elif categ == "SC":
        archivo = open("../recursor/archivos_quizmaker/Sociales.txt", "a")
    elif categ == "CT":
        archivo = open("../recursor/archivos_quizmaker/Cultura.txt", "a")
    else:
        archivo = open("../recursor/archivos_quizmaker/Entretenimiento.txt", "a")

    for pregunta in lista_preguntas:
        archivo.write(pregunta)

    archivo.close()

def almacenar_pregunta(categ, subcateg, nivel, pregunta, answer1, answer2, answer3, answer4):
    """
    Almacena la pregunta y sus datos en el archivo correspondiente a su categoría.
    :param str categ: Categoria corta de la pregunta (CM, SC, ...).
    :param str subcateg: Subcategoria corta de la pregunta (QC, FC, ...).
    :param int nivel: Nivel corto de la pregunta (1 a 3).
    :param str pregunta: Pregunta.
    :param str answer1: Respuesta Correcta.
    :param str answer2: Respuesta incorrecta 1.
    :param str answer3: Respuesta incorrecta 2.
    :param str answer4: Respuesta incorrecta 3.
    """
    vacio = False # Bandera para saber si un archivo está vacío
    linea = "" # Cadena a ser almacenada en el archivo


    if categ == "CM":
        vacio = is_archivo_vacio("Ciencias.txt")
        archivo = open("../recursor/archivos_quizmaker/Ciencias.txt", "a")
    elif categ == "SC":
        vacio = is_archivo_vacio("Sociales.txt")
        archivo = open("../recursor/archivos_quizmaker/Sociales.txt", "a")
    elif categ == "CT":
        vacio = is_archivo_vacio("Cultura.txt")
        archivo = open("../recursor/archivos_quizmaker/Cultura.txt", "a")
    elif categ == "ET":
        vacio = is_archivo_vacio("Entretenimiento.txt")
        archivo = open("../recursor/archivos_quizmaker/Entretenimiento.txt", "a")
 

    if vacio:
        linea = subcateg+"^"+str(nivel)+"^"+pregunta+"^"
        linea += answer1+"^"+answer2+"^"+answer3+"^"+answer4
    else:
        linea = '\n'+subcateg+"^"+str(nivel)+"^"+pregunta+"^"
        linea += answer1+"^"+answer2+"^"+answer3+"^"+answer4

    archivo.write(linea)
    archivo.close()

def crear_archivos():
    """
    Crea los archivos donde se almacenan las preguntas.
    """

    archivo = open("../recursor/archivos_quizmaker/Ciencias.txt", 'a')
    archivo.close()
    archivo = open("../recursor/archivos_quizmaker/Sociales.txt", 'a')
    archivo.close()
    archivo = open("../recursor/archivos_quizmaker/Cultura.txt", 'a')
    archivo.close()
    archivo = open("../recursor/archivos_quizmaker/Entretenimiento.txt", 'a')
    archivo.close()
    archivo = open("../recursor/archivos_quizmaker/Usuarios.txt", 'a')
    archivo.close()

def is_archivo_vacio(nombre):
    """
    Saber si un archivo está vacío.
    :param str nombre: Nombre del archivo.
    :return: True | False
    """
    nombre = "../recursor/archivos_quizmaker/"+nombre
    archivo = open(nombre, "r")
    if archivo.read() == "":
        return True
    archivo.close()
    return False

def is_lista_vacio(lista_cadenas):
    """
    Saber si una lista de cadenas posee mínimo un elemento string vacío ("").
    :param list[string] lista_cadenas: Lista con cadenas.
    :return: True | False
    """
    if "" in lista_cadenas:
        return True
    else:
        return False

def refrescar_contenido(cuadro_texto, categ):
    """
    Refresca el contenido que se muestra en la sección "Quitar pregunta".
    :param Text cuadro_texto: Cuadro donde se muestra el contenido.
    :param str categ: Categoria larga a mostrar (química, física, ...).
    """
    categ = categ[len(categ)-3:len(categ)-1] # Categoría corta
    lista_preguntas = [] # Lista de preguntas para ser mostrada en pantalla
    vacio = False # Bandera para saber si un archivo está vacío

    if categ == "CM":
        vacio = is_archivo_vacio("Ciencias.txt")
        lista_preguntas = leer_archivo("Ciencias.txt")
    elif categ == "SC":
        vacio = is_archivo_vacio("Sociales.txt")
        lista_preguntas = leer_archivo("Sociales.txt")
    elif categ == "CT":
        vacio = is_archivo_vacio("Cultura.txt")
        lista_preguntas = leer_archivo("Cultura.txt")
    else:
        vacio = is_archivo_vacio("Entretenimiento.txt")
        lista_preguntas = leer_archivo("Entretenimiento.txt")

    cont = 0 # Contador
    largo_lista = len(lista_preguntas) # Tamaño de la lista preguntas

    cuadro_texto.delete(1.0, END)

    if vacio:
        cuadro_texto.insert(INSERT, "No hay ninguna pregunta de esta categoría")
    else:
        cuadro_texto.insert(INSERT, "N   Pregunta\t\t\t\tSubcategoría\t\t\t\tNivel\n\n")

        while cont < largo_lista:
            pregunta = lista_preguntas[cont]
            cuadro_texto.insert(INSERT, cont+1)
            cuadro_texto.insert(INSERT, "   " +"¿"+obtener_dato(lista_preguntas, cont, 3)+"?")
            cuadro_texto.insert(INSERT, "\t\t\t" + obtener_dato(lista_preguntas, cont, 1) )
            cuadro_texto.insert(INSERT, "\t\t\t" + obtener_dato(lista_preguntas, cont, 2))
            cuadro_texto.insert(INSERT, '\n')
            cont += 1