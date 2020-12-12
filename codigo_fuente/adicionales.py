import archivos as arch
import registro as reg
import random

def actualzar_datos(usuarios, act_user, rondas, r_won):
    """
    Actualiza la información del usuario.
    :param dict usuarios: Diccionario con usuarios.
    :param str act_user: Usuario actual.
    :param int rondas: Cantidad de rondas jugadas.
    :param int r_won: Cantidad de rondas ganadas.
    """
    kept_r_won = int(usuarios[act_user][1][0]) # Puntaje máximo guardado
    kept_r = int(usuarios[act_user][1][2]) # Rondas puntaje máximo

    punt_max = "" # Puntaje máximo

    if r_won >= kept_r_won:
        if rondas >= kept_r:
            punt_max = str(r_won)+"/"+str(rondas)
        else:
            punt_max = usuarios[act_user][1]
    else:
        punt_max = usuarios[act_user][1]

    rondas += int(usuarios[act_user][2])
    r_won += int(usuarios[act_user][3])

    reg.datos_usuario(act_user, punt_max, rondas, r_won, usuarios)

def obtener_preguntas_juego(num_preguntas=0, categ="none", subcateg="none", nivel=0):
    """
    Obtener preguntas con ciertas caracteristicas para el juego.
    :param int num_preguntas: Cantidad de preguntas a jugar (n >= 1).
    :param str categ: Categoria corta de las preguntas a jugar (CM, SC, ...).
    :param str subcateg: Subcategoria corta de las preguntas a jugar (QC, FC, ...).
    :param int nivel: Nivel corto de las preguntas a jugar (1 a 3).
    :return: list[string]
    """

    if not (is_categoria(categ)):
        categ = "none"

    preguntas_juego = [] # Lista preguntas juego

    if num_preguntas != 0:
        if categ == "CM":
            preguntas_archivo = arch.leer_archivo("Ciencias.txt")
            renglones_preguntas = obtener_renglones(preguntas_archivo, subcateg, nivel)
            lista_aux = []
            while num_preguntas != 0:
                num_random = num_rand(0, len(preguntas_archivo))
                if num_random in renglones_preguntas:
                    lista_aux = []
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 3))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 4))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 5))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 6))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 7))
                    preguntas_juego.append(lista_aux)
                    renglones_preguntas.remove(num_random)
                    num_preguntas -= 1
        elif categ == "SC":
            preguntas_archivo = arch.leer_archivo("Sociales.txt")
            renglones_preguntas = obtener_renglones(preguntas_archivo, subcateg, nivel)
            lista_aux = []
            while num_preguntas != 0:
                num_random = num_rand(0, len(preguntas_archivo))
                if num_random in renglones_preguntas:
                    lista_aux = []
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 3))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 4))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 5))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 6))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 7))
                    preguntas_juego.append(lista_aux)
                    renglones_preguntas.remove(num_random)
                    num_preguntas -= 1
        elif categ == "CT":
            preguntas_archivo = arch.leer_archivo("Cultura.txt")
            renglones_preguntas = obtener_renglones(preguntas_archivo, subcateg, nivel)
            lista_aux = []
            while num_preguntas != 0:
                num_random = num_rand(0, len(preguntas_archivo))
                if num_random in renglones_preguntas:
                    lista_aux = []
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 3))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 4))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 5))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 6))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 7))
                    preguntas_juego.append(lista_aux)
                    renglones_preguntas.remove(num_random)
                    num_preguntas -= 1
        elif categ == "ET":
            preguntas_archivo = arch.leer_archivo("Entretenimiento.txt")
            renglones_preguntas = obtener_renglones(preguntas_archivo, subcateg, nivel)
            lista_aux = []
            while num_preguntas != 0:
                num_random = num_rand(0, len(preguntas_archivo))
                if num_random in renglones_preguntas:
                    lista_aux = []
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 3))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 4))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 5))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 6))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 7))
                    preguntas_juego.append(lista_aux)
                    renglones_preguntas.remove(num_random)
                    num_preguntas -= 1
        elif categ == "none":
            preguntas_archivo = arch.leer_archivo("Ciencias.txt")
            preguntas_archivo.extend(arch.leer_archivo("Sociales.txt"))
            preguntas_archivo.extend(arch.leer_archivo("Cultura.txt"))
            preguntas_archivo.extend(arch.leer_archivo("Entretenimiento.txt"))
            renglones_preguntas = obtener_renglones(preguntas_archivo, nivel=nivel)
            lista_aux = []
            while num_preguntas != 0:
                num_random = num_rand(0, len(preguntas_archivo))
                if num_random in renglones_preguntas:
                    lista_aux = []
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 3))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 4))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 5))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 6))
                    lista_aux.append(arch.obtener_dato(preguntas_archivo, num_random, 7))
                    preguntas_juego.append(lista_aux)
                    renglones_preguntas.remove(num_random)
                    num_preguntas -= 1
                    
        return preguntas_juego
        
def obtener_renglones(lista_preguntas, subcateg = "none", nivel = 0):
    """
    Obtener los índice de la lista donde están las preguntas con ciertas características.
    :param list[string] lista_preguntas: Lista de preguntas.
    :param str subcateg: Subcategoria corta de las preguntas (QC, FC, ...).
    :param int nivel: Nivel corto de las preguntas (1 a 3).
    :return: list[int]
    """
    lista_renglones = [] # Lista renglones de las preguntas que cumplen los requisitos
    for indice in range(len(lista_preguntas)):
        if subcateg == arch.obtener_dato(lista_preguntas, indice, 1) or subcateg == "none":
            if nivel == int(arch.obtener_dato(lista_preguntas, indice, 2)) or nivel == 0:
                lista_renglones.append(indice)
    return lista_renglones

def generar_orden_botones():
    """
    Genera un orden aleatorio de asociamiento entre respuesta y boton (del 0 al 3).
    :return: list[int]
    """
    lista_orden = [] # Lista con orden de los botones
    while len(lista_orden) != 4:
        num_random = num_rand(0,3)
        if num_random not in lista_orden:
            lista_orden.append(num_random)
    return lista_orden
    
def traductor_nivel(nivel):
    """
    Traduce los niveles a números (del 1 al 3).
    :param str nivel: Nivel largo de la pregunta (Facíl, Intermedio, Difícil).
    :return: int
    """
    niv_traducido = 0 # Subcategoría especificada en términos de como se encuentra en el archivo
    nivel = nivel.lower()

    if nivel == "difícil":
        niv_traducido = 3
    elif nivel == "intermedio":
        niv_traducido = 2
    elif nivel == "fácil":
        niv_traducido = 1
    else:
        niv_traducido = 0
    return niv_traducido

def traductor_subcateg(subcateg):
    """
    Traduce las subcategorías y retorna dos caracteres representativos.
    :param str subcateg: Subcategoria larga de la pregunta (química, física, ...).
    :return: str.
    """
    sub_traducida = "" # Subcategoría especificada en términos de como se encuentra en el archivo
    subcateg = subcateg.lower()

    if subcateg == 'química':
        sub_traducida = 'QC'
    elif subcateg == 'física':
         sub_traducida = 'FC'
    elif subcateg == 'biología':
        sub_traducida = 'BG'
    elif subcateg == 'matemáticas':
        sub_traducida = 'MT'
    elif subcateg == 'política':
        sub_traducida = 'PC'
    elif subcateg == 'historia':
        sub_traducida = 'HT'
    elif subcateg == 'geografía':
        sub_traducida = 'GF'
    elif subcateg == 'filosofía':
        sub_traducida = 'FF'
    elif subcateg == 'literatura':
        sub_traducida = 'LT'
    elif subcateg == 'arte':
        sub_traducida = 'AT'
    elif subcateg == 'deportes':
        sub_traducida = 'DP'
    elif subcateg == 'cine':
        sub_traducida = 'CE'
    elif subcateg == 'videojuegos':
        sub_traducida = 'VJ'
    else:
        sub_traducida = "none"

    return sub_traducida 

def contar_subcategoria(lista_preguntas, subcateg):
    """
    Cuenta las preguntas que tienen cierta subcategoría.
    :param list[string] lista_preguntas: Lista que contiene preguntas.
    :param str subcateg: Subcategoría corta de las preguntas a contar (QC, FC, ...).
    :return: int
    """
    cantidad = 0 # Contador
    for indice in range(len(lista_preguntas)):
        if subcateg == arch.obtener_dato(lista_preguntas, indice, 1):
            cantidad += 1
    return cantidad

def contar_nivel(lista_preguntas, nivel, subcateg = "none"):
    """
    Cuenta las preguntas con el nivel y subcategoría especificado.
    :param list[string] lista_preguntas: Lista que contiene las preguntas.
    :param int nivel: Nivel corto de la pregunta (1 - 3).
    :param str subcateg: Subcategoria de las preguntas a contar.
    :return: int
    """
    cantidad = 0 # Contador
    if subcateg != "none":
        for indice in range(len(lista_preguntas)):
            if str(nivel) == arch.obtener_dato(lista_preguntas, indice, 2):
                if subcateg == arch.obtener_dato(lista_preguntas, indice, 1):
                    cantidad += 1 
    else:
        for indice in range(len(lista_preguntas)):
            if str(nivel) == arch.obtener_dato(lista_preguntas, indice, 2):
                cantidad += 1 
    return cantidad
       
def contar_preguntas(categ='none', subcateg='none', nivel=0) :
    """
    Cuenta el número de preguntas en el archivo con ciertas características.
    :param str categ: Categoria corta de las preguntas (CM, SC, ..).
    :param str subcateg: Subcategoria corta de las preguntas (QC, FC, ...).
    :param int nivel: Nivel corto de la pregunta (1 - 3).
    :return: int
    """
    cantidad_preguntas = 0 # Cantidad de preguntas
    lista_preguntas = [] # Lista con preguntas

    if categ == 'CM':
        lista_preguntas = arch.leer_archivo("Ciencias.txt")
    elif categ == 'SC':
        lista_preguntas = arch.leer_archivo("Sociales.txt")
    elif categ == 'CT':
        lista_preguntas = arch.leer_archivo("Cultura.txt")
    elif categ == 'ET':
        lista_preguntas = arch.leer_archivo("Entretenimiento.txt")
    else:
        if nivel == 0:
            lista_preguntas1 = arch.leer_archivo("Ciencias.txt")
            cantidad_preguntas += contar(lista_preguntas1)

            lista_preguntas2 = arch.leer_archivo("Sociales.txt")
            cantidad_preguntas += contar(lista_preguntas2)

            lista_preguntas3 = arch.leer_archivo("Cultura.txt")
            cantidad_preguntas += contar(lista_preguntas3)

            lista_preguntas4 = arch.leer_archivo("Entretenimiento.txt")
            cantidad_preguntas += contar(lista_preguntas4)
            return cantidad_preguntas
        else:
            lista_preguntas1 = arch.leer_archivo("Ciencias.txt")
            cantidad_preguntas += contar_nivel(lista_preguntas1, nivel)

            lista_preguntas2 = arch.leer_archivo("Sociales.txt")
            cantidad_preguntas += contar_nivel(lista_preguntas2, nivel)

            lista_preguntas3 = arch.leer_archivo("Cultura.txt")
            cantidad_preguntas += contar_nivel(lista_preguntas3, nivel)

            lista_preguntas4 = arch.leer_archivo("Entretenimiento.txt")
            cantidad_preguntas += contar_nivel(lista_preguntas4, nivel)

            return cantidad_preguntas

    if subcateg == 'none' and nivel == 0:
        cantidad_preguntas += contar(lista_preguntas)
    elif subcateg != 'none' and nivel == 0:
        cantidad_preguntas = contar_subcategoria(lista_preguntas, subcateg)
    elif subcateg == 'none' and nivel != 0:
        cantidad_preguntas = contar_nivel(lista_preguntas, nivel)
    else:
        cantidad_preguntas = contar_nivel(lista_preguntas, nivel, subcateg)

    return cantidad_preguntas

def cambiar_frame(frame_show, frame_hide):
    """
    Habilita el frame "frame_habilitar" y esconde el frame "frame_esconder".
    :param Frame frame_habilitar: Frame a habilitar.
    :param Frame frame_esconder: Frame a esconder.
    """
    frame_hide.pack_forget()
    frame_show.pack()

def cerrar_GUI(raiz):
    """
    Elimina la raiz y cierra la GUI.
    :param Tk raiz: Raiz.
    """
    raiz.destroy()

def is_caracteres(lista_cadenas, lista_caracteres):
    """
    Busca si algun caracter se encuentra mínimo una vez en alguna cadena.
    :param list[string] lista_cadenas: Cadenas a evaluar.
    :param list[string] lista_caracteres: Caracteres a buscar en las cadenas.
    :return: True | False
    """
    for caracter in lista_caracteres:
        for cadena in lista_cadenas:
            if is_caracter(cadena, caracter):
                return True
    return False

def is_categoria(categ):
    """
    Saber si una cadena representa una categoría de pregunta.
    :param str categ: Categoría corta de la pregunta (CM, SC, ...)
    :return: True | False
    """
    if categ in "CM SC CT ET":
        return True
    return False

#  Generar número aleatorio
num_rand = lambda min,max: random.randint(min, max)

# Cuenta las preguntas de una lista
contar = lambda lista_preguntas : len(lista_preguntas)

# Saber si un caracter está contenido en un string
is_caracter = lambda cadena, carac : carac in cadena