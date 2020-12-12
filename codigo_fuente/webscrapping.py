from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

#Funciones para realizar el WebScraping

def scrapear():
    '''
    Función compuesta de distintas funciones que scrapea la página que se eligió para el proyecto y 
    genera varios archivos que son de interés para el programa.
    :param bool archivos_creados: Saber si ya existen los archivos necesarios.
    '''
    
    url = "https://ocio.uncomo.com/articulo/preguntas-de-cultura-general-con-respuestas-49522.html"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = (BeautifulSoup(html, "html.parser"))
    informacion=str(soup)

    scrap=open('../recursor/archivos_quizmaker/archivo.html','w')
    scrap.write(informacion)
    scrap.close()

    texto = soup.get_text()
    text_scrap=open('../recursor/archivos_quizmaker/preguntas_scrap.txt','w')
    text_scrap.write(texto)
    text_scrap.close()
    text_scrap=open('../recursor/archivos_quizmaker/preguntas_scrap.txt','r')
    lineas_archivo=text_scrap.readlines()
    text_scrap.close()
    guardar_preguntas(lineas_archivo)

def guardar_preguntas(lineas_archivo):
    '''
    Guarda y clasifica en un archivo las preguntas dependiendo de su categoría
    :param list[str] lineas_archivo: Son las líneas del archivo de texto extraído de la página.
    '''
    sociales=extraer_info(lineas_archivo,2)
    almacenar_sociales(sociales)
    cultura=extraer_info(lineas_archivo,3)
    almacenar_categorias(cultura,'CULTURA')
    entretenimiento=extraer_info(lineas_archivo,4)
    almacenar_categorias(entretenimiento,'ENTRETENIMIENTO')
    ciencias=extraer_info(lineas_archivo,5)
    almacenar_categorias(ciencias,'CIENCIAS')

def extraer_info(contenido_archivo,categoria):
    '''
    Sirve para extraer la información que nos interesa, es decir las preguntas que se encuentran en el 
    archivo.
    :param list[str] contenido_archivo: el contenido leído de un archivo de texto.
    :param str categoria: es la categoría en mayúsculas a buscar.
    :return: list[str]
    '''
    lista=[]
    for contenido in contenido_archivo:
        if len(contenido)>100:
            lista.append(contenido)
    lista_preguntas=preguntas(lista[categoria])
    return lista_preguntas

def preguntas(parrafo):
    '''
    Función que separa las preguntas de un párrafo específico.
    :param string parrafo: Es un párrafo de preguntas continuas de una misma categoría.
    :return: list[str]
    '''
    lista_preguntas=parrafo.split('¿')
    return lista_preguntas

def adecuar_cadena(cadena):
    '''
    Funciona para eliminar las tildes y caracteres no deseados en el programa, pues adapta la cadena a 
    la funcionalidad del programa.
    :param str cadena: cadena de texto que contiene la pregunta y la respuesta.
    :return: str.
    '''
    reemplazar_caracteres = {("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"),('ñ','ni'),('? ','^'),('(',''),(')','')}
    for primer, segundo in reemplazar_caracteres:
        cadena = cadena.replace(primer, segundo).replace(primer.upper(), segundo.upper())
    return cadena

def almacenar_sociales(sociales):
    '''
    Almacena las preguntas de la categoría sociales en un archivo que se crea en esta misma función
    :param str sociales: Representa la categoría a guardar en el archivo.
    '''
    preguntas_scrap=open('../recursor/archivos_quizmaker/preguntas_scrap.txt','w')
    del sociales[0]
    preguntas_scrap.write('COMIENZA_SOCIALES\n')
    for pregunta in sociales:
        if pregunta == sociales[len(sociales)-1]:
            preguntas_scrap.write(adecuar_cadena(pregunta)+'TERMINA_SOCIALES')
        else:
            preguntas_scrap.write(adecuar_cadena(pregunta)+'\n')
    preguntas_scrap.close()

def almacenar_categorias(lista_categoria,categoria):
    '''
    Almacena las preguntas de las categorías en un archivo de texto donde están todas las preguntas,
    la función se encarga de organizar las preguntas en el formato que se ha estado utilizando en el 
    proyecto.
    :param list[str] lista_categoria: es una lista de las preguntas de una misma categoría.
    :param str categoria: representa la categoría a guardar en el archivo.
    '''
    del lista_categoria[0]
    preguntas_scrap=open('../recursor/archivos_quizmaker/preguntas_scrap.txt','a')
    preguntas_scrap.write('\nCOMIENZA_'+categoria+'\n')
    for pregunta in lista_categoria:
        if pregunta == lista_categoria[len(lista_categoria)-1]:
            preguntas_scrap.write(adecuar_cadena(pregunta)+'TERMINA_'+categoria)
        else:
            preguntas_scrap.write(adecuar_cadena(pregunta)+'\n')
    preguntas_scrap.close()

#Funciones para utilizar los archivos creados después del WebScrap

def extraer_pregunta(categoria):
    '''
    Sirve para obtener una pregunta al azar dentro de una categoría especifica.
    :param str categoria: un string en mayúscula de la categoría en la cual se quiere obtener
    una pregunta.
    :return: str, str
    '''
    preguntas_scrap=open('../recursor/archivos_quizmaker/preguntas_scrap.txt','r')
    limite_sup,limite_inf=encontrar_categoria(categoria)
    renglon=random.randint(limite_sup+1, limite_inf-1)
    preguntas=preguntas_scrap.readlines()
    pregunta_azar=preguntas[renglon]
    pregunta_azar=pregunta_azar.split('^')
    pregunta=pregunta_azar[0]
    respuesta=pregunta_azar[1]
    return pregunta,respuesta[:len(respuesta)-1]

def encontrar_categoria(categoria):
    '''
    Funciona para encontrar los renglones entre los que están contenidas las preguntas
    de una categoría especificada.
    :param str categoria: un string en mayúscula de la categoría en la cual se quiere obtener
    una pregunta.
    return int, int
    '''
    if categoria=='CIENCIAS':
        comienzo='COMIENZA_'+categoria+'\n'
        final='TERMINA_'+categoria
    else:
        comienzo='COMIENZA_'+categoria+'\n'
        final='TERMINA_'+categoria+'\n'
    preguntas_scrap=open('../recursor/archivos_quizmaker/preguntas_scrap.txt','r')
    lineas=preguntas_scrap.readlines()
    iterador=0
    for linea in lineas:
        if linea==comienzo:
            begin=iterador
        if linea==final:
            end=iterador
        iterador+=1
    return begin,end