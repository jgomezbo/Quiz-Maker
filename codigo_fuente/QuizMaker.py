"""
Quiz Maker

Johan Danilo Gómez Bocanegra
Luis Fernando Chitiva Arévalo
Daniel Ricardo Quintero Moya
"""

# Librerias
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
#from datetime import datetime
#now = datetime.now()

"""
from tkinter import font
#Ver fuentes de texto disponibles
root = tk.Tk()
for font in font.families():
    print(font)
"""
# Creando GUI
def crear_GUI():
    """
    Crea la ventana principal de la GUI con el frame 1 activado.
    """
    ancho = "800" # Ancho frame1
    alto = "500"  # Alto frame1
    color = "#ff9933" # Color frame1
    separx_F1 = 5  # Separación de witgets con limites contenedor en x Frame 1
    separy_F1 = 12  # Separación de witgets con limites contenedor en y Frame 1
    separx_F2 = 12  # Separación de witgets con limites contenedor en x Frame 2
    separy_F2 = 14  # Separación de witgets con limites contenedor en y Frame 2
    separx_F3 = 20  # Separación de witgets con limites contenedor en x Frame 3
    separy_F3 = 25  # Separación de witgets con limites contenedor en y Frame 3
    separx_F4 = 12  # Separación de witgets con limites contenedor en x Frame 4
    separy_F4 = 8   # Separación de witgets con limites contenedor en y Frame 4
    separy_F5 = 8   # Separación de witgets con limites contenedor en y Frame 5
    separy_F6 = 25   # Separación de witgets con limites contenedor en y Frame 6

    # Creando raiz
    raiz = Tk()
    raiz.title("Quiz Maker")
    raiz.resizable(0,0)
    raiz.config(bg=f"{color}")
    raiz.iconbitmap("icono.ico")
    raiz.geometry(ancho+"x"+alto)

    # Creando frame1 (Menú) -------------------------------------------------------------------------------------
    frame1 = Frame(raiz)
    frame1.config(width=ancho, height=alto, bg=color, cursor="arrow")
    frame1.pack(fill="y", expand="True")
        
    # Creando titulo portada
    titulo_portada = Label(frame1, text="Quiz Maker", fg="green", bg=color, font=("Ravie",60))
    titulo_portada.grid(row=0, column=0, pady=separy_F1, padx=separx_F1)

    # Creando botones
    boton_empezar = Button(frame1, text="Empezar", fg="black", bg="#27BF39", font=("Arial",25), command = lambda:cambiar_frame(frame6, frame1))
    boton_empezar.config(cursor="hand2")
    boton_empezar.grid(row=1, column=0, pady=separy_F1, padx=separx_F1)
    
    boton_preguntas = Button(frame1, text="Preguntas", fg="black", bg="#27BF39", font=("Arial",25), command=lambda:cambiar_frame(frame3,frame1))
    boton_preguntas.config(cursor="hand2")
    boton_preguntas.grid(row=2, column=0, pady=separy_F1, padx=separx_F1)

    boton_instrucciones = Button(frame1, text="Instrucciones", fg="black", bg="#27BF39", font=("Arial",25), command=lambda:cambiar_frame(frame2,frame1))
    boton_instrucciones.config(cursor="hand2")
    boton_instrucciones.grid(row=3, column=0, pady=separy_F1, padx=separx_F1)

    boton_salir = Button(frame1, text="Salir", fg="black", bg="#E8220F", font=("Arial",20), command=lambda:cerrar_GUI(raiz))
    boton_salir.config(cursor="hand2")
    boton_salir.grid(row=4, column=0, pady=separy_F1, padx=separx_F1, sticky="w")

    # Creando frame2 (Instrucciones) -------------------------------------------------------------------------------------
    frame2 = Frame(raiz)
    frame2.config(width=ancho, height=alto, bg=color, cursor="arrow")
        
    # Creando titulo portada
    titulo_instrucciones = Label(frame2, text=texto_instrucciones, fg="black", bg=color, font=("Comic Sans MS",11))
    titulo_instrucciones.grid(row=0, column=0, pady=separy_F2, padx=separx_F2)

    # Creando botones
    boton_volver1 = Button(frame2, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command=lambda:cambiar_frame(frame1,frame2))
    boton_volver1.config(cursor="hand2")
    boton_volver1.grid(row=2, column=0, pady=separy_F2, padx=separx_F2, sticky="sw")

    # Creando frame3 (Preguntas) -------------------------------------------------------------------------------------
    frame3 = Frame(raiz)
    frame3.config(width=ancho, height=alto, bg=color, cursor="arrow")
    
    # Creando título preguntas
    titulo_preguntas = Label(frame3, text="Preguntas", fg="black", bg=color, font=("Arial",30))
    titulo_preguntas.grid(row=0, column=0, pady=separy_F3, padx=separx_F3, columnspan=2)

    # Creando subtítulos preguntas
    subtitulo1_preguntas = Label(frame3, text="Agregar pregunta", fg="black", bg=color, font=("Arial",15))
    subtitulo1_preguntas.grid(row=1, column=0, pady=separy_F3, padx=separx_F3, sticky="w")

    subtitulo2_preguntas = Label(frame3, text="Quitar pregunta", fg="black", bg=color, font=("Arial",15))
    subtitulo2_preguntas.grid(row=1, column=1, pady=separy_F3, padx=separx_F3, sticky="e")

    boton_volver3 = Button(frame3, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command=lambda:cambiar_frame(frame1, frame3))
    boton_volver3.config(cursor="hand2")
    boton_volver3.grid(row=3, column=0, pady=separy_F3, padx=separx_F3, sticky="s")

    # Creando botones

    boton_agregar = Button(frame3, text="Agregar", fg="black", bg="#70B824", font=("Arial",20), command=lambda:cambiar_frame(frame4, frame3))
    boton_agregar.config(cursor="hand2")
    boton_agregar.grid(row=2, column=0)
    boton_quitar = Button(frame3, text="Quitar", fg="black", bg="#E33524", font=("Arial",20), command=lambda:cambiar_frame(frame5, frame3))
    boton_quitar.config(cursor="hand2")
    boton_quitar.grid(row=2, column=1)

    # Creando frame4 (agregar pregunta) -------------------------------------------------------------------------------------
    frame4 = Frame(raiz)
    frame4.config(width=ancho, height=alto, bg=color, cursor="arrow") 

    # Creando título
    Label(frame4, text="Agregar pregunta", fg="black", bg=color, font=("Arial",30)).grid(row=0, column=0, pady=separy_F4, padx=separx_F4, columnspan=2)

    # Creando botones( y textos
    Label(frame4, text='Ingrese la pregunta (NO poner "¿ ? ^"): ', fg="black", bg=color, font=("Arial",12)).grid(row=1, column=0, pady=separy_F4)
    entry1_f4 = Entry(frame4, width=40)
    entry1_f4.grid(row=1, column=1, pady=separy_F4)

    Label(frame4, text='Ingrese la respuesta correcta: ', fg="black", bg=color, font=("Arial",12)).grid(row=2, column=0, pady=separy_F4)
    entry2_f4 = Entry(frame4, width=40)
    entry2_f4.grid(row=2, column=1, pady=separy_F4)

    Label(frame4, text='Ingrese otra respuesta: ', fg="black", bg=color, font=("Arial",12)).grid(row=3, column=0, pady=separy_F4)
    entry3_f4 = Entry(frame4, width=40)
    entry3_f4.grid(row=3, column=1, pady=separy_F4)

    Label(frame4, text='Ingrese otra respuesta: ', fg="black", bg=color, font=("Arial",12)).grid(row=4, column=0, pady=separy_F4)
    entry4_f4 = Entry(frame4, width=40)
    entry4_f4.grid(row=4, column=1, pady=separy_F4)

    Label(frame4, text='Ingrese otra respuesta: ', fg="black", bg=color, font=("Arial",12)).grid(row=5, column=0, pady=separy_F4)
    entry5_f4 = Entry(frame4, width=40)
    entry5_f4.grid(row=5, column=1, pady=separy_F4)

    # Creado combobox 1 (Dificultad)
    Label(frame4, text="Dificultad de la pregunta: ", fg="black", bg=color, font=("Arial",12)).grid(row=6, column=0, pady=separy_F4)

    combobox1_f4 = ttk.Combobox(frame4) 
    combobox1_f4["values"]=("Fácil", "Intermedio", "Difícil")
    combobox1_f4.current(0)
    combobox1_f4.grid(row=6, column=1, pady=separy_F4)

    # Creando combobox 2 (Categoría)
    Label(frame4, text="Categoría: ", fg="black", bg=color, font=("Arial",12)).grid(row=7, column=0, pady=separy_F4)

    combobox2_f4 = ttk.Combobox(frame4) 
    combobox2_f4.config(width=35)
    combobox2_f4["values"]=("Ciencias Naturales / Matemáticas (CM)", "Ciencias Sociales (SC)", "Cultura (CT)", "Entretenimiento (ET)")
    combobox2_f4.current(0)
    combobox2_f4.grid(row=7, column=1, pady=separy_F4)

    # Creando combobox 3 (Subcategoría)
    Label(frame4, text="Subcategoría: ", fg="black", bg=color, font=("Arial",12)).grid(row=8, column=0, pady=separy_F4)

    combobox3_f4 = ttk.Combobox(frame4) 
    combobox3_f4["values"]=("(CM) Química", "(CM) Física", "(CM) Biología", "(CM) Matemáticas", "(SC) Política", "(SC) Historia", "(SC) Geografía", "(SC) filosofía", "(CT) Literatura", "(CT) Arte", "(ET) Deportes", "(ET) Cine", "(ET) Videojuegos")
    combobox3_f4.current(0)
    combobox3_f4.grid(row=8, column=1, pady=separy_F4)

    # Creando botones
    boton_volver3 = Button(frame4, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command=lambda:cambiar_frame(frame3, frame4))
    boton_volver3.config(cursor="hand2")
    boton_volver3.grid(row=9, column=0, pady=separy_F4)

    boton_guardar1 = Button(frame4, text="Guardar", fg="black", bg="#70B824", font=("Arial",20), command=lambda :comprobar_pregunta(entry1_f4.get(),entry2_f4.get(),entry3_f4.get(),entry4_f4.get(),entry5_f4.get(),combobox1_f4.get(),combobox2_f4.get(),combobox3_f4.get()))
    boton_guardar1.config(cursor="hand2")
    boton_guardar1.grid(row=9, column=1, pady=separy_F4)

    # Creando frame5 (quitar pregunta) -------------------------------------------------------------------------------------
    frame5 = Frame(raiz)
    frame5.config(width=ancho, height=alto, bg=color, cursor="arrow") 

    # Creando título
    Label(frame5, text="Quitar pregunta", fg="black", bg=color, font=("Arial",30)).grid(row=0, column=0, pady=separy_F5, columnspan=2)

    # Creando cuadro de texto
    cuadro_texto = Text(frame5, height=10)
    cuadro_texto.grid(row=1, column=0, columnspan=2)

    # Creando Scrollbar vertical y horizontal
    scroll_vertical = Scrollbar(frame5, orient='vertical', command=cuadro_texto.yview)
    scroll_vertical.grid(row=1, column=1, sticky="nse")

    scroll_horizontal = Scrollbar(frame5, orient='horizontal', command=cuadro_texto.xview)
    scroll_horizontal.grid(row=2, column=0, columnspan=2, sticky="new")

    # Creando combobox

    Label(frame5, text='Categoria: ', fg="black", bg=color, font=("Arial",12)).grid(row=3, column=0)
    combobox1_f5 = ttk.Combobox(frame5) 
    combobox1_f5.config(width=35)
    combobox1_f5["values"]=("Ciencias Naturales / Matemáticas (CM)", "Ciencias Sociales (SC)", "Cultura (CT)", "Entretenimiento (ET)")
    combobox1_f5.current(0)
    combobox1_f5.grid(row=3, column=1, pady=separy_F5)

    # Creando Button "Refrescar"
    boton_refrescar = Button(frame5, text="Refrescar", fg="black", bg="#307295", font=("Arial",20), command = lambda:refrescar_contenido(cuadro_texto, combobox1_f5.get()))
    boton_refrescar.config(cursor="hand2")
    boton_refrescar.grid(row=4, column=0, columnspan=2, pady=separy_F5)

    # Creando Entry "Eliminar pregunta"
    Label(frame5, text='Eliminar pregunta (dígite el número): ', fg="black", bg=color, font=("Arial",12)).grid(row=5, column=0, sticky="e")
    entry1_f5 = Entry(frame5)
    entry1_f5.grid(row=5, column=1, pady=separy_F5)

    # Creando Buttons "Eliminar" y "Volver"
    boton_volver4 = Button(frame5, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command = lambda:cambiar_frame(frame3, frame5))
    boton_volver4.config(cursor="hand2")
    boton_volver4.grid(row=6, column=0, pady=separy_F5)

    boton_eliminar = Button(frame5, text="Eliminar", fg="black", bg="#E33524", font=("Arial",20), command = lambda:eliminar_pregunta(combobox1_f5.get(), entry1_f5.get()))
    boton_eliminar.grid(row=6, column=1, pady=separy_F5)

    # Creando frame6 (Empezar) -------------------------------------------------------------------------------------
    frame6 = Frame(raiz)
    frame6.config(width=ancho, height=alto, bg=color, cursor="arrow") 

    # Creando "Labels"
    Label(frame6, text='Tipo de partida:', fg="black", bg=color, font=("Arial",12)).grid(row=0, column=0, pady=separy_F6)
    Label(frame6, text='Categoría:', fg="black", bg=color, font=("Arial",12)).grid(row=1, column=0, pady=separy_F6)
    Label(frame6, text='Subcategoría:', fg="black", bg=color, font=("Arial",12)).grid(row=2, column=0, pady=separy_F6)
    Label(frame6, text='Nivel:', fg="black", bg=color, font=("Arial",12)).grid(row=3, column=0, pady=separy_F6)
    Label(frame6, text='Cantidad de preguntas a jugar:', fg="black", bg=color, font=("Arial",12)).grid(row=4, column=0, pady=separy_F6)

    # Creando "Comboboxes"
    combobox1_f6 = ttk.Combobox(frame6) 
    combobox2_f6 = ttk.Combobox(frame6) 
    combobox3_f6 = ttk.Combobox(frame6) 
    combobox4_f6 = ttk.Combobox(frame6) 

    combobox1_f6.config(width=35)
    combobox2_f6.config(width=35)
    combobox3_f6.config(width=35)
    combobox4_f6.config(width=35)

    combobox1_f6["values"]=("Selección-Múltiple")
    combobox2_f6["values"]=("Cualquiera", "Ciencias Naturales / Matemáticas (CM)", "Ciencias Sociales (SC)", "Cultura (CT)", "Entretenimiento (ET)")
    combobox3_f6["values"]=("Cualquiera", "(CM) Química", "(CM) Física", "(CM) Biología", "(CM) Matemáticas", "(SC) Política", "(SC) Historia", "(SC) Geografía", "(SC) filosofía", "(CT) Literatura", "(CT) Arte", "(ET) Deportes", "(ET) Cine", "(ET) Videojuegos")
    combobox4_f6["values"]=("Cualquiera", "Fácil", "Intermedio", "Difícil")

    combobox1_f6.current(0)
    combobox2_f6.current(0)
    combobox3_f6.current(0)
    combobox4_f6.current(0)

    combobox1_f6.grid(row=0, column=1, pady=separy_F6)
    combobox2_f6.grid(row=1, column=1, pady=separy_F6)
    combobox3_f6.grid(row=2, column=1, pady=separy_F6)
    combobox4_f6.grid(row=3, column=1, pady=separy_F6)

    # Creando "Spinbox"
    spinbox_f6 = Spinbox(frame6, from_=1, to=100, width=10)
    spinbox_f6.grid(row=4, column=1, pady=separy_F6)

    # Creando "Buttons"

    boton_volver5 = Button(frame6, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command = lambda:cambiar_frame(frame1, frame6))
    boton_volver5.config(cursor="hand2")
    boton_volver5.grid(row=5, column=0, pady=separy_F6)

    boton_jugar = Button(frame6, text="Jugar", fg="black", bg="#70B824", font=("Arial",20), command = lambda:verificar_jugar(frame7, frame6, combobox1_f6.get(), combobox2_f6.get(), combobox3_f6.get(), combobox4_f6.get(), int(spinbox_f6.get()), [label_pregunta, boton_azul, boton_rojo, boton_verde, boton_amarillo, score]))
    boton_jugar.config(cursor="hand2")
    boton_jugar.grid(row=5, column=1, pady=separy_F6)

    # Creando frame7 (Juego: Selección múltiple) -------------------------------------------------------------------------------------
    frame7 = Frame(raiz)
    frame7.config(width=ancho, height=alto, bg=color, cursor="arrow") 

    # Pregunta
    label_pregunta = Label(frame7, text="La pregunta es muy buen porque podría someter cualquier cosa", fg="black", bg="#D4A3FC", font=("Cooper Black",14), width=64, height=4)
    label_pregunta.grid(row=0, column=0, columnspan=2)

    # Creando "Buttons"
    boton_azul = Button(frame7, width=34, height=6, bg="#4DA3F0", fg="black", font=("Cooper Black",13), command = lambda:boton_seleccionado("azul", [label_pregunta, boton_azul, boton_rojo, boton_verde, boton_amarillo, score, frame1, frame7]))
    boton_rojo = Button(frame7, width=34, height=6, bg="#EF5B5B", fg="black", font=("Cooper Black",13), command = lambda:boton_seleccionado("rojo", [label_pregunta, boton_azul, boton_rojo, boton_verde, boton_amarillo, score, frame1, frame7]))
    boton_verde = Button(frame7, width=34, height=6, bg="#6DF04D", fg="black", font=("Cooper Black",13), command = lambda:boton_seleccionado("verde", [label_pregunta, boton_azul, boton_rojo, boton_verde, boton_amarillo, score, frame1, frame7]))
    boton_amarillo = Button(frame7, width=34, height=6, bg="#F0E64D", fg="black", font=("Cooper Black",13), command = lambda:boton_seleccionado("amarillo", [label_pregunta, boton_azul, boton_rojo, boton_verde, boton_amarillo, score, frame1, frame7]))

    boton_azul.grid(row=1, column=0, sticky="w", padx=0)
    boton_rojo.grid(row=1, column=1, sticky="e", padx=0)
    boton_verde.grid(row=2, column=0, sticky="w", padx=0)
    boton_amarillo.grid(row=2, column=1, sticky="e", padx=0)

    boton_azul.config(cursor="dot")
    boton_rojo.config(cursor="dot")
    boton_verde.config(cursor="dot")
    boton_amarillo.config(cursor="dot")

    # Label "Score"
    score = Label(frame7, text="Score: 0", fg="black", bg=color, font=("Cooper Black",30))
    score.grid(row=3, column=0, pady=50)


    # Mantener a la escucha la GUI
    raiz.mainloop()

def boton_seleccionado(color, widgets):
    """
    Recibe un valor del boton selecccionado.
    :param str color: Color del boton seleccionado.
    :param Tk widgets: Widgets del frame 6.
    """
    seleccion_multiple(color, widgets)

ronda = 1 # Ronda actual
score_juego = 0 # Puntaje en el juego
lista_preguntas_juegos = [] # Lista de preguntas del juego
orden_botones = [] # Orden de las respuestas

def seleccion_multiple(color, widgets):
    """
    Ejecuta el juego de selección múltiple
    :param list[string] lista_preguntas: Lista con preguntas.
    :param Tk widgets: Widgets del frame 6.
    """
    global lista_preguntas_juegos
    global ronda
    global score_juego
    global orden_botones

    if color == "azul":
        if orden_botones[0] == 0:
            score_juego += 1
        orden_botones = generar_orden_botones()
        ronda += 1
        color = "none"

    elif color == "rojo":
        if orden_botones[1] == 0:
            score_juego += 1
        orden_botones = generar_orden_botones()
        ronda += 1
        color = "none"

    elif color == "verde":
        if orden_botones[2] == 0:
            score_juego += 1
        orden_botones = generar_orden_botones()
        ronda += 1
        color = "none"

    elif color == "amarillo":
        if orden_botones[3] == 0:
            score_juego += 1
        orden_botones = generar_orden_botones()
        ronda += 1
        color = "none"

    if ronda > len(lista_preguntas_juegos):
        messagebox.showinfo("Juego completado", "Tu puntaje ha sido de "+str(score_juego)+"/"+str(ronda-1))
        ronda = 1
        lista_preguntas_juegos = []
        score_juego = 0 
        cambiar_frame(widgets[6], widgets[7])
        return

    widgets[0].config(text="¿"+lista_preguntas_juegos[ronda-1][0]+"?")
    widgets[1].config(text=lista_preguntas_juegos[ronda-1][orden_botones[0]+1])
    widgets[2].config(text=lista_preguntas_juegos[ronda-1][orden_botones[1]+1])
    widgets[3].config(text=lista_preguntas_juegos[ronda-1][orden_botones[2]+1])
    widgets[4].config(text=lista_preguntas_juegos[ronda-1][orden_botones[3]+1])
    widgets[5].config(text="Score: "+str(score_juego))

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
            preguntas_archivo = leer_archivo("Ciencias.txt")
            renglones_preguntas = obtener_renglones(preguntas_archivo, subcateg, nivel)
            lista_aux = []
            while num_preguntas != 0:
                num_random = num_rand(0, len(preguntas_archivo))
                if num_random in renglones_preguntas:
                    lista_aux = []
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 3))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 4))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 5))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 6))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 7))
                    preguntas_juego.append(lista_aux)
                    renglones_preguntas.remove(num_random)
                    num_preguntas -= 1
        elif categ == "SC":
            preguntas_archivo = leer_archivo("Sociales.txt")
            renglones_preguntas = obtener_renglones(preguntas_archivo, subcateg, nivel)
            lista_aux = []
            while num_preguntas != 0:
                num_random = num_rand(0, len(preguntas_archivo))
                if num_random in renglones_preguntas:
                    lista_aux = []
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 3))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 4))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 5))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 6))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 7))
                    preguntas_juego.append(lista_aux)
                    renglones_preguntas.remove(num_random)
                    num_preguntas -= 1
        elif categ == "CT":
            preguntas_archivo = leer_archivo("Cultura.txt")
            renglones_preguntas = obtener_renglones(preguntas_archivo, subcateg, nivel)
            lista_aux = []
            while num_preguntas != 0:
                num_random = num_rand(0, len(preguntas_archivo))
                if num_random in renglones_preguntas:
                    lista_aux = []
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 3))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 4))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 5))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 6))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 7))
                    preguntas_juego.append(lista_aux)
                    renglones_preguntas.remove(num_random)
                    num_preguntas -= 1
        elif categ == "ET":
            preguntas_archivo = leer_archivo("Entretenimiento.txt")
            renglones_preguntas = obtener_renglones(preguntas_archivo, subcateg, nivel)
            lista_aux = []
            while num_preguntas != 0:
                num_random = num_rand(0, len(preguntas_archivo))
                if num_random in renglones_preguntas:
                    lista_aux = []
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 3))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 4))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 5))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 6))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 7))
                    preguntas_juego.append(lista_aux)
                    renglones_preguntas.remove(num_random)
                    num_preguntas -= 1
        elif categ == "none":
            preguntas_archivo = leer_archivo("Ciencias.txt")
            preguntas_archivo.extend(leer_archivo("Sociales.txt"))
            preguntas_archivo.extend(leer_archivo("Cultura.txt"))
            preguntas_archivo.extend(leer_archivo("Entretenimiento.txt"))
            renglones_preguntas = obtener_renglones(preguntas_archivo, nivel=nivel)
            lista_aux = []
            while num_preguntas != 0:
                num_random = num_rand(0, len(preguntas_archivo))
                if num_random in renglones_preguntas:
                    lista_aux = []
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 3))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 4))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 5))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 6))
                    lista_aux.append(obtener_dato(preguntas_archivo, num_random, 7))
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
        if subcateg == obtener_dato(lista_preguntas, indice, 1) or subcateg == "none":
            if nivel == int(obtener_dato(lista_preguntas, indice, 2)) or nivel == 0:
                lista_renglones.append(indice)
    return lista_renglones

def verificar_jugar(frame_show, frame_hide, juego, categ, subcateg, nivel, num_preguntas, widgets):
    """
    Verifica los datos ingresados antes de empezar el juego.
    :param list[Frame] frame_show: Lista de Frames de los juegos.
    :param Frame frame_hide: Frame actual (Frame 6).
    :param str juego: Juego para presentar las preguntas.
    :param str categ: Categoria de las preguntas a jugar.
    :param str subcateg: Subcategoria de las preguntas a jugar.
    :param str nivel: Nivel largo de las preguntas a jugar (facíl, intermedio, ...).
    :param int num_preguntas: Cantidad de preguntas a jugar.
    :param Tk widgets: Widgets del frame 6.
    """
    global lista_preguntas_juegos
    global orden_botones

    mas_preguntas = False # Bandera para saber si existen le número de preguntas solicitadas
    categ_larga = categ[:] # Categoría larga
    categ = categ[len(categ)-3:len(categ)-1] # Categoría corta
    subcateg_larga = subcateg[:] # Subcategoría larga
    categ_subcateg = subcateg[1:3] # Categoría corta de la subcategoría
    subcateg = traductor_subcateg(subcateg[5:]) # Subcategoría corta
    trad_nivel = traductor_nivel(nivel) # Nivel corto (1 a 3)

    if (categ == categ_subcateg) and nivel != "Cualquiera":
        if num_preguntas <= contar_preguntas(categ, subcateg, trad_nivel):
            mas_preguntas = True

    elif (categ == categ_subcateg) and nivel == "Cualquiera":
        if num_preguntas <= contar_preguntas(categ, subcateg):
            mas_preguntas = True

    elif categ_larga != "Cualquiera" and subcateg_larga == "Cualquiera" and nivel != "Cualquiera":
        if num_preguntas <= contar_preguntas(categ, nivel=trad_nivel):
            mas_preguntas = True

    elif categ_larga != "Cualquiera" and subcateg_larga == "Cualquiera" and nivel == "Cualquiera":
        if num_preguntas <= contar_preguntas(categ):
            mas_preguntas = True

    elif categ_larga == "Cualquiera" and subcateg_larga == "Cualquiera" and nivel != "Cualquiera":
        if num_preguntas <= contar_preguntas(nivel=trad_nivel):
            mas_preguntas = True

    elif categ_larga == "Cualquiera" and subcateg_larga == "Cualquiera" and nivel == "Cualquiera":
        if num_preguntas <= contar_preguntas():
            mas_preguntas = True

    elif categ_larga == "Cualquiera" and subcateg_larga != "Cualquiera":
        messagebox.showerror("Error", "Si elige categoría 'Cualquiera', la subcategoría también deben ser 'Cualquiera")
        return
    else:
        messagebox.showerror("Error","Verifique que la categoría y subcategoría sean compatibles")
        return

    if mas_preguntas:
        if juego == "Selección-Múltiple":
            lista_preguntas_juegos = obtener_preguntas_juego(num_preguntas, categ, subcateg, trad_nivel)
            orden_botones = generar_orden_botones()
            cambiar_frame(frame_show, frame_hide)
            seleccion_multiple("none", widgets)
            return
    else:
        messagebox.showerror("Error","No hay suficientes preguntas con esas características")

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
    else:
        messagebox.showerror("Error", "Verifique que no hayan espacios en blanco")

def guardar_lista_archivo(categ, lista_preguntas):
    """
    Guarda el contenido de una lista en el archivo.
    :param str categ: Categoría corta del archivo a guardar el contenido de la lista (CM, SC, ...).
    :param list[string] lista_preguntas: Lista de preguntas para ser almacenadas.
    """
    if categ == "CM":
        archivo = open("Ciencias.txt", "a")
    elif categ == "SC":
        archivo = open("Sociales.txt", "a")
    elif categ == "CT":
        archivo = open("Cultura.txt", "a")
    else:
        archivo = open("Entretenimiento.txt", "a")

    for pregunta in lista_preguntas:
        archivo.write(pregunta)

    archivo.close()

def borrar_contenido_archivo(categ):
    """
    Borra todo el contenido de un archivo.
    :param str categ: Categoría corta del archivo para borrar el contenido (CM, SC, ...).
    """
    if categ == "CM":
        archivo = open("Ciencias.txt", "w")
    elif categ == "SC":
        archivo = open("Sociales.txt", "w")
    elif categ  == "CT":
        archivo = open("Cultura.txt", "w")
    else:
        archivo = open("Entretenimiento.txt", "w")
    archivo.close()

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
        if subcateg == obtener_dato(lista_preguntas, indice, 1):
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
            if str(nivel) == obtener_dato(lista_preguntas, indice, 2):
                if subcateg == obtener_dato(lista_preguntas, indice, 1):
                    cantidad += 1 
    else:
        for indice in range(len(lista_preguntas)):
            if str(nivel) == obtener_dato(lista_preguntas, indice, 2):
                cantidad += 1 
    return cantidad

def leer_archivo(nombre):
    """
    Leer contenido de un archivo.
    :param str nombre: Nombre del archivo ("nombre.txt").
    :return: list[string]
    """
    archivo = open(nombre,'r')
    lista_preguntas = archivo.readlines()
    return lista_preguntas
       
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
        lista_preguntas = leer_archivo("Ciencias.txt")
    elif categ == 'SC':
        lista_preguntas = leer_archivo("Sociales.txt")
    elif categ == 'CT':
        lista_preguntas = leer_archivo("Cultura.txt")
    elif categ == 'ET':
        lista_preguntas = leer_archivo("Entretenimiento.txt")
    else:
        if nivel == 0:
            lista_preguntas1 = leer_archivo("Ciencias.txt")
            cantidad_preguntas += contar(lista_preguntas1)

            lista_preguntas2 = leer_archivo("Sociales.txt")
            cantidad_preguntas += contar(lista_preguntas2)

            lista_preguntas3 = leer_archivo("Cultura.txt")
            cantidad_preguntas += contar(lista_preguntas3)

            lista_preguntas4 = leer_archivo("Entretenimiento.txt")
            cantidad_preguntas += contar(lista_preguntas4)
            return cantidad_preguntas
        else:
            lista_preguntas1 = leer_archivo("Ciencias.txt")
            cantidad_preguntas += contar_nivel(lista_preguntas1, nivel)

            lista_preguntas2 = leer_archivo("Sociales.txt")
            cantidad_preguntas += contar_nivel(lista_preguntas2, nivel)

            lista_preguntas3 = leer_archivo("Cultura.txt")
            cantidad_preguntas += contar_nivel(lista_preguntas3, nivel)

            lista_preguntas4 = leer_archivo("Entretenimiento.txt")
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

def comprobar_pregunta(pregunta, answer1, answer2, answer3, answer4, nivel, categ, subcateg):
    """
    Comprueba que los datos sean correctos para ser almacenados.
    :param str pregunta: Pregunta.
    :param str answer1: Respuesta correcta.
    :param str answer2: Respuesta incorrecta 1.
    :param str answer3: Respuesta incorrecta 2.
    :param str answer4: Respuesta incorrecta 3.
    :param int nivel: Nivel largo de la pregunta (fácil, intermedio, ...).
    :param str categ: Categoría larga de la pregunta.
    :param str subcateg: Subcategoría larga de la pregunta.
    """
    categ = categ[len(categ)-3:len(categ)-1] # Categoría corta
    categ_subcateg = subcateg[1:3] # Categoría corta de la subcategoría
    subcateg = traductor_subcateg(subcateg[5:]) # Subcategoría corta

    if is_lista_vacio([pregunta, answer1, answer2, answer3, answer4]):
        messagebox.showerror("Error","Verifique que no hayan espacios en blanco")
    else:
        if is_caracteres([pregunta, answer1, answer2, answer3, answer4], ['?', '¿', '^']):
            messagebox.showerror("Error","Verifique que las entradas NO contengan '?', '¿' y '^'")
        else:
            if categ == categ_subcateg:
                niv_traducido = traductor_nivel(nivel)
                almacenar_pregunta(categ, subcateg, niv_traducido, pregunta, answer1, answer2, answer3, answer4)
                messagebox.showinfo("Guardado correcto","La pregunta ha sido guardada exitosamente")
                return
            else:
                messagebox.showerror("Error","Verifique que la categoría y subcategoría sean compatibles")
                return

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

def is_archivo_vacio(nombre):
    """
    Saber si un archivo está vacío.
    :param str nombre: Nombre del archivo.
    :return: True | False
    """
    archivo = open(nombre, "r")
    if archivo.read() == "":
        return True
    archivo.close()
    return False

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
        archivo = open("Ciencias.txt", "a")
    elif categ == "SC":
        vacio = is_archivo_vacio("Sociales.txt")
        archivo = open("Sociales.txt", "a")
    elif categ == "CT":
        vacio = is_archivo_vacio("Cultura.txt")
        archivo = open("Cultura.txt", "a")
    elif categ == "ET":
        vacio = is_archivo_vacio("Entretenimiento.txt")
        archivo = open("Entretenimiento.txt", "a")

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
    archivo = open("Ciencias.txt", 'a')
    archivo.close()
    archivo = open("Sociales.txt", 'a')
    archivo.close()
    archivo = open("Cultura.txt", 'a')
    archivo.close()
    archivo = open("Entretenimiento.txt", 'a')
    archivo.close()

#  Generar número aleatorio
num_rand = lambda min,max: random.randint(min, max)

# Cuenta las preguntas de una lista
contar = lambda lista_preguntas : len(lista_preguntas)

# Saber si un caracter está contenido en un string
is_caracter = lambda cadena, carac : carac in cadena

# Función main o principal
def main():
    """
    Función principal.
    """
    crear_archivos()
    crear_GUI()

# Texto de instrucciones
texto_instrucciones="""Quiz Maker es un aplicativo que te permite realizar quices de forma didáctica en 
diferentes presentaciones.

Para poder empezar a usar el aplicativo correctamente, se deben seguir los siguientes pasos:

1). Dar clic en el botón "Preguntas" en el menú.
2). En la sección de preguntas puede "agregar" o "quitar" preguntas. Si desea agregar,
de clic en la opción "Agregar", posteriormente, ingrese su pregunta, respuesta correcta
con otras tres (incorrectas), categoría, subcategoría y dificultad.
3). Para quitar preguntas de clic en la opción "Quitar", posteriormente seleccione la categoría
y de pulse en "Refrescar" para que aparescan las preguntas que contiene la categoría. Seleccione.
Digite el número de la pregunta y pulse "Eliminar".
4). De clic en "Empezar" en el menú, a continuación, seleccione el tipo de quiz
y que tipo de preguntas quiere que aparescan en al quiz.
5). De clic en "Jugar" y !aprende y disfruta con los quices!

Quiz Maker®. Johan Gómez, Luis Chitiva, Daniel Quintero. All rights reserved & copyright © 2020.
"""

# Ejecución de todo el programa
main()
