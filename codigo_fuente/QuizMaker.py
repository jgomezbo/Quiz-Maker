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
import time
import pygame

# Librerías propias
import archivos as arch # Módulo que maneja los archivos
import registro as reg # Módulo que maneja los usuarios y contraseñas
import webscrapping as web # Módulo que maneja información de la web
import adicionales as adic # Módulo con funciones adicionales

pygame.mixer.init()

# Creando GUI
def crear_GUI():
    """
    Crea la ventana principal de la GUI con el frame 1 activado.
    """
    ancho = "800" # Ancho frame1
    alto = "550"  # Alto frame1
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

    usuarios =  {}
    reg.archivo_a_diccionario(usuarios) # Usuarios

    global act_user # Usuario actual
    act_user = ""

    global ronda # Ronda actual
    global score_juego # Puntaje en el juego
    global lista_preguntas_juegos # Lista de preguntas del juego
    global orden_botones # Orden de las respuestas
    global inicia # Saber si el juego ya inició"""
    global ronda # Ronda actual

    ronda = 1 
    score_juego = 0 
    lista_preguntas_juegos = [] 
    orden_botones = [] 
    inicia = False

    texto_instrucciones = "" #Instrucciones

    admin_user = "quizmaker2020" # Usuario admin
    admin_password = "me copie en el parcial" # Contraseña de admin

    try: 
        archivo = open("../recursor/archivos_quizmaker/Instrucciones.txt",'r')
        texto_instrucciones = archivo.read()
        archivo.close()
    except:
        texto_instrucciones = " Error"

    # Creando raiz
    raiz = Tk()
    raiz.title("Quiz Maker")
    raiz.resizable(0,0)
    raiz.config(bg=f"{color}")
    raiz.iconbitmap("../recursor/imagenes/icono.ico")
    raiz.geometry(ancho+"x"+alto)

    pygame.mixer.music.load("../recursor/sonidos/BonusLevel.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=-1)

    # Creando frame_Admin (modo admin)
    frame_admin = Frame(raiz)
    frame_admin.config(width=ancho, height=alto, bg=color, cursor="arrow")

    # Creando cuadro de texto
    contenido_admin = Text(frame_admin, width = 80, height = 20)
    contenido_admin.grid(row = 0, column = 0, pady = separy_F5)

    # Creando Scrollbar vertical y horizontal
    scroll_vertical = Scrollbar(frame_admin, orient='vertical', command=contenido_admin.yview)
    scroll_vertical.grid(row=0, column=1, sticky="nse", pady = separy_F5)

    # Creando entries
    user_del = Entry(frame_admin, width = 30)
    user_del.grid(row = 1, column = 0, pady = separy_F5, sticky = "w")

    # Creando botones
    del_boton = Button(frame_admin, text="Eliminar", fg="black", bg="#E33524", font=("Arial",20), command=lambda:eliminar_user())
    del_boton.config(cursor="hand2")
    del_boton.grid(row = 1, column = 0, pady = separy_F5, sticky = "e")

    def eliminar_user():
        user = user_del.get()
        if user in usuarios:
            del(usuarios[user])
            reg.almacenar_usuarios(usuarios)
            messagebox.showinfo("Borrado exitoso", "El usuario fue eliminado exitosamente")

    refrescar_del = Button(frame_admin, text = "Refrescar", fg="black", bg="#307295", font=("Arial",20), command=lambda:refrescar_info())
    refrescar_del.config(cursor="hand2")
    refrescar_del.grid(row = 2, column = 0, columnspan = 2, pady = separy_F5)

    def refrescar_info():
        contenido_admin.delete(1.0, END)

        cont = 0 # contador
        largo_lista = len(usuarios) # Largo dict
        vacio = False

        if usuarios == {}:
            vacio = True

        if vacio:
            contenido_admin.insert(INSERT, "No hay ningun usuario registrado")
        else:
            contenido_admin.insert(INSERT, "Usuario\t\t\tMáx Score\t\tRounds\t\tRounds won\n\n")

            list_users = list(usuarios.keys())
            list_users.sort()

            for key in list_users:
                contenido_admin.insert(INSERT, key)
                contenido_admin.insert(INSERT, "\t\t\t"+usuarios[key][1])
                contenido_admin.insert(INSERT, "\t\t"+str(usuarios[key][2]))
                contenido_admin.insert(INSERT, "\t\t"+str(usuarios[key][3]))
                contenido_admin.insert(INSERT, '\n')

    # Creando frame0 (Usuarios)
    frame0 = Frame(raiz)
    frame0.config(width=ancho, height=alto, bg=color, cursor="arrow")
    frame0.pack()

    # Creando botones

    titulo_portada1 = Label(frame0, text="Quiz Maker", fg="green", bg=color, font=("Ravie",60))
    titulo_portada1.grid(row=0, column=0, pady=separy_F1, padx=separx_F1)   

    boton_signin = Button(frame0, text="Registrarse", fg="black", bg="#27BF39", font=("Arial",25), command = lambda:adic.cambiar_frame(frame_sign, frame0))
    boton_signin.config(cursor="hand2")
    boton_signin.grid(row=2, column=0, pady=separy_F1, padx=separx_F1) 

    boton_login = Button(frame0, text="Iniciar sesión", fg="black", bg="#27BF39", font=("Arial",25), command = lambda:adic.cambiar_frame(frame_log, frame0))
    boton_login.config(cursor="hand2")
    boton_login.grid(row=1, column=0, pady=separy_F1, padx=separx_F1) 

    boton_salir1 = Button(frame0, text="Salir", fg="black", bg="#E8220F", font=("Arial",20), command=lambda:adic.cerrar_GUI(raiz))
    boton_salir1.config(cursor="hand2")
    boton_salir1.grid(row=4, column=0, pady=separy_F1, padx=separx_F1, sticky="w")

    # Creando signin (registro)
    frame_sign = Frame(raiz)
    frame_sign.config(width=ancho, height=alto, bg=color, cursor="arrow")

    titulo_sign = Label(frame_sign, text="Registro", fg="Black", bg=color, font=("Ravie",60))
    titulo_sign.grid(row=0, column=0, pady=separy_F1, columnspan=2)   

    nombre_sign = Label(frame_sign, text="Usuario", fg="black", bg=color, font=("Arial",15))
    nombre_sign.grid(row=1, column=0, pady=separy_F3, padx=separx_F3, sticky="w")

    password_sign = Label(frame_sign, text="Contraseña", fg="black", bg=color, font=("Arial",15))
    password_sign.grid(row=2, column=0, pady=separy_F3, padx=separx_F3, sticky="w")

    # Creando entries

    entry1_fsign = Entry(frame_sign, width=40)
    entry1_fsign.grid(row=1, column=1, pady=separy_F4)

    entry2_fsign = Entry(frame_sign, width=40)
    entry2_fsign.grid(row=2, column=1, pady=separy_F4)

    # Creando botones

    boton_registrar = Button(frame_sign, text="Registrar", fg="black", bg="#70B824", font=("Arial",20), command=lambda:registrar_usuario())
    boton_registrar.config(cursor="hand2")
    boton_registrar.grid(row=3, column=1, pady=separy_F3, padx=separx_F3, sticky="s")

    def registrar_usuario():
        """
        Registra usuario nuevo.
        """
        global act_user

        user = entry1_fsign.get()
        password = entry2_fsign.get()

        if adic.is_caracteres([user, password], ['¿','?','^','\n']):
            messagebox.showerror('Error', "No use los caracteres '?', '¿' y '^'")
            return

        if user == admin_user:
            messagebox.showerror('Error', 'El usuario ingresado ya existe')
            return

        estado = reg.registro_usuario(user, password, usuarios)
        if estado:
            reg.almacenar_usuarios(usuarios)
            act_user = user
            adic.cambiar_frame(frame1, frame_sign)
        else:
            messagebox.showerror('Error', 'El usuario ingresado ya existe')

    boton_volver_sign = Button(frame_sign, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command=lambda:adic.cambiar_frame(frame0, frame_sign))
    boton_volver_sign.config(cursor="hand2")
    boton_volver_sign.grid(row=3, column=0, pady=separy_F3, padx=separx_F3, sticky="s")

    # Creando login (iniciar sesión)
    frame_log = Frame(raiz)
    frame_log.config(width=ancho, height=alto, bg=color, cursor="arrow")

    titulo_log = Label(frame_log, text="Sesión", fg="Black", bg=color, font=("Ravie",60))
    titulo_log.grid(row=0, column=0, pady=separy_F1, padx=separx_F1, columnspan=2) 

    nombre_log = Label(frame_log, text="Usuario", fg="black", bg=color, font=("Arial",15))
    nombre_log.grid(row=1, column=0, pady=separy_F3, padx=separx_F3, sticky="w")

    password_log = Label(frame_log, text="Contraseña", fg="black", bg=color, font=("Arial",15))
    password_log.grid(row=2, column=0, pady=separy_F3, padx=separx_F3, sticky="w")

    # Creando entries

    entry1_flog = Entry(frame_log, width=40)
    entry1_flog.grid(row=1, column=1, pady=separy_F4)

    entry2_flog = Entry(frame_log, width=40)
    entry2_flog.grid(row=2, column=1, pady=separy_F4)

    # Creando botones

    boton_iniciar_log = Button(frame_log, text="Iniciar", fg="black", bg="#70B824", font=("Arial",20), command=lambda:iniciar_usuario())
    boton_iniciar_log.config(cursor="hand2")
    boton_iniciar_log.grid(row=3, column=1, pady=separy_F3, padx=separx_F3, sticky="s")

    def iniciar_usuario():

        global act_user

        user = entry1_flog.get()
        password = entry2_flog.get()

        estado, num = reg.comprobar_usuario(user, password, usuarios)

        if estado:
            act_user = user
            adic.cambiar_frame(frame1, frame_log)
        else:
            if is_admin(user, password):
                act_user = user
                adic.cambiar_frame(frame_admin, frame_log)
                messagebox.showinfo("Modo admin", "Usted se encuentra en modo administrador")
                return

            if num == 1:
                messagebox.showerror('Error', 'El usuario NO existe')
            else:
                messagebox.showerror('Error', 'La contraseña es INCORRECTA')
    
    def is_admin(user, password):
        if user == admin_user:
            if password == admin_password:
                return True
        return False    

    boton_volver_log = Button(frame_log, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command=lambda:adic.cambiar_frame(frame0, frame_log))
    boton_volver_log.config(cursor="hand2")
    boton_volver_log.grid(row=3, column=0, pady=separy_F3, padx=separx_F3, sticky="s")

    # Creando frame1 (Menú) -------------------------------------------------------------------------------------
    frame1 = Frame(raiz)
    frame1.config(width=ancho, height=alto, bg=color, cursor="arrow")
        
    # Creando titulo portada
    titulo_portada = Label(frame1, text="Quiz Maker", fg="green", bg=color, font=("Ravie",60))
    titulo_portada.grid(row=0, column=0, pady=separy_F1, padx=separx_F1)

    # Creando botones
    boton_empezar = Button(frame1, text="Empezar", fg="black", bg="#27BF39", font=("Arial",25), command = lambda:adic.cambiar_frame(frame6, frame1))
    boton_empezar.config(cursor="hand2")
    boton_empezar.grid(row=1, column=0, pady=separy_F1, padx=separx_F1)
    
    boton_preguntas = Button(frame1, text="Preguntas", fg="black", bg="#27BF39", font=("Arial",25), command=lambda:adic.cambiar_frame(frame3,frame1))
    boton_preguntas.config(cursor="hand2")
    boton_preguntas.grid(row=2, column=0, pady=separy_F1, padx=separx_F1)

    boton_instrucciones = Button(frame1, text="Instrucciones", fg="black", bg="#27BF39", font=("Arial",25), command=lambda:adic.cambiar_frame(frame2,frame1))
    boton_instrucciones.config(cursor="hand2")
    boton_instrucciones.grid(row=3, column=0, pady=separy_F1, padx=separx_F1, sticky = "w")

    boton_estadisticas = Button(frame1, text="Estadisticas", fg="black", bg="#27BF39", font=("Arial",25), command=lambda:ver_estadisticas())
    boton_estadisticas.config(cursor="hand2")
    boton_estadisticas.grid(row=3, column=0, pady=separy_F1, padx=separx_F1, sticky = "e")

    def ver_estadisticas():
        """
        carga pantalla de estadisticas.
        """
        l_user_v.set("Usuario:    "+act_user)
        l_max_score_v.set("Mejor puntaje:    "+usuarios[act_user][1])
        l_rounds_v.set("Rondas jugadas:    "+str(usuarios[act_user][2]))
        l_rounds_won_v.set("Rondas ganadas:    "+str(usuarios[act_user][3]))
        adic.cambiar_frame(f_estadistica,frame1)

    boton_salir = Button(frame1, text="Salir", fg="black", bg="#E8220F", font=("Arial",20), command=lambda:adic.cerrar_GUI(raiz))
    boton_salir.config(cursor="hand2")
    boton_salir.grid(row=4, column=0, padx=separx_F1, sticky = "w")

    # Creando f_estadistica (Estadisticas) -------------------------------------------------------------------------------------
    f_estadistica = Frame(raiz)
    f_estadistica.config(width=ancho, height=alto, bg=color, cursor="arrow")

    # Creando título preguntas
    titulo_preguntas = Label(f_estadistica, text="Estadísticas", fg="black", bg=color, font=("Arial",30))
    titulo_preguntas.grid(row=0, column=0, pady=separy_F3, padx=separx_F3, columnspan=2)

    # Creando mensajes
    l_user_v = StringVar()
    l_user = Label(f_estadistica, bg=color, font=("Arial",20), textvariable = l_user_v)
    l_user.grid(row = 1, column = 0, pady=separy_F2)

    l_max_score_v = StringVar()
    l_max_score = Label(f_estadistica, bg=color, font=("Arial",20), textvariable = l_max_score_v)
    l_max_score.grid(row = 2, column = 0, pady=separy_F2)

    l_rounds_v = StringVar()
    l_rounds = Label(f_estadistica, bg=color, font=("Arial",20), textvariable = l_rounds_v)
    l_rounds.grid(row = 3, column = 0, pady=separy_F2)

    l_rounds_won_v = StringVar()
    l_rounds_won = Label(f_estadistica, bg=color, font=("Arial",20), textvariable = l_rounds_won_v)
    l_rounds_won.grid(row = 4, column = 0, pady=separy_F2)

    # Creando botones

    boton_volver_e = Button(f_estadistica, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command=lambda:adic.cambiar_frame(frame1,f_estadistica))
    boton_volver_e.config(cursor="hand2")
    boton_volver_e.grid(row=5, column=0, pady=separy_F2, padx=separx_F2+70, sticky="sw")

    # Creando frame2 (Instrucciones) -------------------------------------------------------------------------------------
    frame2 = Frame(raiz)
    frame2.config(width=ancho, height=alto, bg=color, cursor="arrow")
        
    # Creando titulo portada
    titulo_instrucciones = Label(frame2, text=texto_instrucciones, fg="black", bg=color, font=("Comic Sans MS",11))
    titulo_instrucciones.grid(row=0, column=0, pady=separy_F2, padx=separx_F2)

    # Creando botones
    boton_volver1 = Button(frame2, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command=lambda:adic.cambiar_frame(frame1,frame2))
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

    boton_volver3 = Button(frame3, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command=lambda:adic.cambiar_frame(frame1, frame3))
    boton_volver3.config(cursor="hand2")
    boton_volver3.grid(row=3, column=0, pady=separy_F3, padx=separx_F3, sticky="s")

    # Creando botones

    boton_agregar = Button(frame3, text="Agregar", fg="black", bg="#70B824", font=("Arial",20), command=lambda:adic.cambiar_frame(frame4, frame3))
    boton_agregar.config(cursor="hand2")
    boton_agregar.grid(row=2, column=0)
    boton_quitar = Button(frame3, text="Quitar", fg="black", bg="#E33524", font=("Arial",20), command=lambda:adic.cambiar_frame(frame5, frame3))
    boton_quitar.config(cursor="hand2")
    boton_quitar.grid(row=2, column=1)

    # Creando frame4 (agregar pregunta) -------------------------------------------------------------------------------------
    frame4 = Frame(raiz)
    frame4.config(width=ancho, height=alto, bg=color, cursor="arrow") 

    # Creando título
    Label(frame4, text="Agregar pregunta", fg="black", bg=color, font=("Arial",30)).grid(row=0, column=0, pady=separy_F4, padx=separx_F4, columnspan=3)

    # Creando botones y textos
    Label(frame4, text='Ingrese la pregunta (NO poner "¿ ? ^"): ', fg="black", bg=color, font=("Arial",12)).grid(row=1, column=0, pady=separy_F4)
    texto_f4 = StringVar()
    entry1_f4 = Entry(frame4, width=40, textvariable = texto_f4)
    entry1_f4.grid(row=1, column=1, pady=separy_F4)

    Label(frame4, text='Ingrese la respuesta correcta: ', fg="black", bg=color, font=("Arial",12)).grid(row=2, column=0, pady=separy_F4)
    texto2_f4 = StringVar()
    entry2_f4 = Entry(frame4, width=40, textvariable = texto2_f4)
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

    def cambiar_comboboxf4_subcategoria(event):
        """
        Cambia combobox de subcategoria dependiendo de la categoría en frame 4.
        """
        actual = combobox2_f4.current()
        if actual == 0:
            comboCM_f4.grid(row=8, column=1, pady=separy_F4)
            comboSC_f4.grid_remove()
            comboCT_f4.grid_remove()
            comboET_f4.grid_remove()
        elif actual == 1:
            comboCM_f4.grid_remove()
            comboSC_f4.grid(row=8, column=1, pady=separy_F4)
            comboCT_f4.grid_remove()
            comboET_f4.grid_remove()
        elif actual == 2:
            comboCM_f4.grid_remove()
            comboSC_f4.grid_remove()
            comboCT_f4.grid(row=8, column=1, pady=separy_F4)
            comboET_f4.grid_remove()
        elif actual == 3:
            comboCM_f4.grid_remove()
            comboSC_f4.grid_remove()
            comboCT_f4.grid_remove()
            comboET_f4.grid(row=8, column=1, pady=separy_F4)

    combobox2_f4.bind("<<ComboboxSelected>>", cambiar_comboboxf4_subcategoria)

    # Creando combobox 3 (Subcategoría)
    Label(frame4, text="Subcategoría: ", fg="black", bg=color, font=("Arial",12)).grid(row=8, column=0, pady=separy_F4)

    comboCM_f4 = ttk.Combobox(frame4) 
    comboCM_f4["values"]=("(CM) Química", "(CM) Física", "(CM) Biología", "(CM) Matemáticas")
    comboCM_f4.current(0)
    comboCM_f4.grid(row=8, column=1, pady=separy_F4)

    comboSC_f4 = ttk.Combobox(frame4) 
    comboSC_f4["values"]=("(SC) Política", "(SC) Historia", "(SC) Geografía", "(SC) filosofía")
    comboSC_f4.current(0)

    comboCT_f4 = ttk.Combobox(frame4) 
    comboCT_f4["values"]=("(CT) Literatura", "(CT) Arte")
    comboCT_f4.current(0)

    comboET_f4 = ttk.Combobox(frame4) 
    comboET_f4["values"]=("(ET) Deportes", "(ET) Cine", "(ET) Videojuegos")
    comboET_f4.current(0)

    # Creando botones

    boton_aleatorio = Button(frame4, text="Aleatorio", fg="black", bg="#307295", font=("Arial",20), command=lambda:pregunta_aleatoria())
    boton_aleatorio.config(cursor="hand2")
    boton_aleatorio.grid(row = 9, column = 2, padx = 20)

    def pregunta_aleatoria():
        """
        Ajusta una pregunta aleatoria de la web en pantalla.
        """
        categ = combobox2_f4.get()

        datos = () # Datos de la web

        if categ == "Ciencias Naturales / Matemáticas (CM)":
            datos = web.extraer_pregunta("CIENCIAS")
        elif categ == "Ciencias Sociales (SC)":
            datos = web.extraer_pregunta("SOCIALES")
        elif categ == "Cultura (CT)":
            datos = web.extraer_pregunta("CULTURA")
        elif categ == "Entretenimiento (ET)":
            datos = web.extraer_pregunta("ENTRETENIMIENTO")

        texto_f4.set(datos[0])
        texto2_f4.set(datos[1])
        
    boton_volver3 = Button(frame4, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command=lambda:adic.cambiar_frame(frame3, frame4))
    boton_volver3.config(cursor="hand2")
    boton_volver3.grid(row=9, column=0, pady=separy_F4)

    def comprobar_pregunta():   
        """
        Comprueba que los datos sean correctos para ser almacenados.
        """
        pregunta, answer1 = entry1_f4.get(), entry2_f4.get()
        answer2, answer3, answer4 = entry3_f4.get(), entry4_f4.get(), entry5_f4.get()
        nivel, categ = combobox1_f4.get(), combobox2_f4.get()
        subcateg = ""

        actual = combobox2_f4.current() # Seleccion actual

        if actual == 0:
            subcateg = comboCM_f4.get()
        elif actual == 1:
            subcateg = comboSC_f4.get()
        elif actual == 2:
            subcateg = comboCT_f4.get()
        elif actual == 3:
            subcateg = comboET_f4.get()

        categ = categ[len(categ)-3:len(categ)-1] # Categoría corta
        categ_subcateg = subcateg[1:3] # Categoría corta de la subcategoría
        subcateg = adic.traductor_subcateg(subcateg[5:]) # Subcategoría corta

        if arch.is_lista_vacio([pregunta, answer1, answer2, answer3, answer4]):
            messagebox.showerror("Error","Verifique que no hayan espacios en blanco")
        else:
            if adic.is_caracteres([pregunta, answer1, answer2, answer3, answer4], ['?', '¿', '^']):
                messagebox.showerror("Error","Verifique que las entradas NO contengan '?', '¿' y '^'")
            else:
                if categ == categ_subcateg:
                    niv_traducido = adic.traductor_nivel(nivel)
                    arch.almacenar_pregunta(categ, subcateg, niv_traducido, pregunta, answer1, answer2, answer3, answer4)
                    messagebox.showinfo("Guardado correcto","La pregunta ha sido guardada exitosamente")
                    return
                else:
                    messagebox.showerror("Error","Verifique que la categoría y subcategoría sean compatibles")
                    return

    boton_guardar1 = Button(frame4, text="Guardar", fg="black", bg="#70B824", font=("Arial",20), command=lambda :comprobar_pregunta())
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

    # Creando combobox

    Label(frame5, text='Categoria: ', fg="black", bg=color, font=("Arial",12)).grid(row=3, column=0)
    combobox1_f5 = ttk.Combobox(frame5) 
    combobox1_f5.config(width=35)
    combobox1_f5["values"]=("Ciencias Naturales / Matemáticas (CM)", "Ciencias Sociales (SC)", "Cultura (CT)", "Entretenimiento (ET)")
    combobox1_f5.current(0)
    combobox1_f5.grid(row=3, column=1, pady=separy_F5)

    # Creando Button "Refrescar"
    boton_refrescar = Button(frame5, text="Refrescar", fg="black", bg="#307295", font=("Arial",20), command = lambda:arch.refrescar_contenido(cuadro_texto, combobox1_f5.get()))
    boton_refrescar.config(cursor="hand2")
    boton_refrescar.grid(row=4, column=0, columnspan=2, pady=separy_F5)

    # Creando Entry "Eliminar pregunta"
    Label(frame5, text='Eliminar pregunta (dígite el número): ', fg="black", bg=color, font=("Arial",12)).grid(row=5, column=0, sticky="e")
    entry1_f5 = Entry(frame5)
    entry1_f5.grid(row=5, column=1, pady=separy_F5)

    # Creando Buttons "Eliminar" y "Volver"
    boton_volver4 = Button(frame5, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command = lambda:adic.cambiar_frame(frame3, frame5))
    boton_volver4.config(cursor="hand2")
    boton_volver4.grid(row=6, column=0, pady=separy_F5)

    boton_eliminar = Button(frame5, text="Eliminar", fg="black", bg="#E33524", font=("Arial",20), command = lambda:arch.eliminar_pregunta(combobox1_f5.get(), entry1_f5.get()))
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
    combobox4_f6 = ttk.Combobox(frame6) 

    combobox1_f6.config(width=35)
    combobox2_f6.config(width=35)
    combobox4_f6.config(width=35)

    combobox1_f6["values"]=("Selección-Múltiple")
    combobox2_f6["values"]=("Cualquiera", "Ciencias Naturales / Matemáticas (CM)", "Ciencias Sociales (SC)", "Cultura (CT)", "Entretenimiento (ET)")
    combobox4_f6["values"]=("Cualquiera", "Fácil", "Intermedio", "Difícil")

    combobox1_f6.current(0)
    combobox2_f6.current(0)
    combobox4_f6.current(0)

    combobox1_f6.grid(row=0, column=1, pady=separy_F6)
    combobox2_f6.grid(row=1, column=1, pady=separy_F6)
    combobox4_f6.grid(row=3, column=1, pady=separy_F6)

    comboCM_f6 = ttk.Combobox(frame6) 
    comboSC_f6 = ttk.Combobox(frame6) 
    comboCT_f6 = ttk.Combobox(frame6) 
    comboET_f6 = ttk.Combobox(frame6) 

    comboCM_f6.config(width=35)
    comboSC_f6.config(width=35)
    comboCT_f6.config(width=35)
    comboET_f6.config(width=35)

    comboCM_f6["values"]=("Cualquiera", "(CM) Química", "(CM) Física", "(CM) Biología", "(CM) Matemáticas")
    comboSC_f6["values"]=("Cualquiera", "(SC) Política", "(SC) Historia", "(SC) Geografía", "(SC) filosofía")
    comboCT_f6["values"]=("Cualquiera", "(CT) Literatura", "(CT) Arte")
    comboET_f6["values"]=("Cualquiera", "(ET) Deportes", "(ET) Cine", "(ET) Videojuegos")

    comboCM_f6.current(0)
    comboSC_f6.current(0)
    comboCT_f6.current(0)
    comboET_f6.current(0)

    def cambiar_comboboxf6_subcategoria(event):
        """
        Cambia combobox de subcategoria dependiendo de la categoría en frame 6.
        """
        actual = combobox2_f6.current()

        if actual == 0:
            comboCM_f6.grid_remove()
            comboSC_f6.grid_remove()
            comboCT_f6.grid_remove()
            comboET_f6.grid_remove()
        elif actual == 1:
            comboCM_f6.grid(row=2, column=1, pady=separy_F6)
            comboSC_f6.grid_remove()
            comboCT_f6.grid_remove()
            comboET_f6.grid_remove()
        elif actual == 2:
            comboCM_f6.grid_remove()
            comboSC_f6.grid(row=2, column=1, pady=separy_F6)
            comboCT_f6.grid_remove()
            comboET_f6.grid_remove()
        elif actual == 3:
            comboCM_f6.grid_remove()
            comboSC_f6.grid_remove()
            comboCT_f6.grid(row=2, column=1, pady=separy_F6)
            comboET_f6.grid_remove()
        elif actual == 4:
            comboCM_f6.grid_remove()
            comboSC_f6.grid_remove()
            comboCT_f6.grid_remove()
            comboET_f6.grid(row=2, column=1, pady=separy_F6)

    combobox2_f6.bind("<<ComboboxSelected>>", cambiar_comboboxf6_subcategoria)

    # Creando "Spinbox"
    spinbox_f6 = Spinbox(frame6, from_=1, to=100, width=10)
    spinbox_f6.grid(row=4, column=1, pady=separy_F6)

    # Creando "Buttons" 

    boton_volver5 = Button(frame6, text="Volver", fg="black", bg="#a0a0a0", font=("Arial",20), command = lambda:adic.cambiar_frame(frame1, frame6))
    boton_volver5.config(cursor="hand2")
    boton_volver5.grid(row=5, column=0, pady=separy_F6)

    def verificar_jugar(frame_show, frame_hide):
        """
        Verifica los datos ingresados antes de empezar el juego.
        :param list[Frame] frame_show: Lista de Frames de los juegos.
        :param Frame frame_hide: Frame actual (Frame 6).
        """
        global lista_preguntas_juegos
        global orden_botones

        juego, categ = combobox1_f6.get(), combobox2_f6.get()
        nivel, num_preguntas = combobox4_f6.get(), int(spinbox_f6.get())
        widgets = [label_pregunta, boton_azul, boton_rojo, boton_verde, boton_amarillo, score]
        subcateg = "Cualquiera"

        if combobox2_f6.current(0) == 1:
            subcateg = comboCM_f6.get()
        elif combobox2_f6.current(0) == 2:
            subcateg = comboSC_f6.get()
        elif combobox2_f6.current(0) == 3:
            subcateg = comboCT_f6.get()
        elif combobox2_f6.current(0) == 4:
            subcateg = comboET_f6.get()

        mas_preguntas = False # Bandera para saber si existen le número de preguntas solicitadas
        categ_larga = categ[:] # Categoría larga
        categ = categ[len(categ)-3:len(categ)-1] # Categoría corta
        subcateg_larga = subcateg[:] # Subcategoría larga
        categ_subcateg = subcateg[1:3] # Categoría corta de la subcategoría
        subcateg = adic.traductor_subcateg(subcateg[5:]) # Subcategoría corta
        trad_nivel = adic.traductor_nivel(nivel) # Nivel corto (1 a 3)

        if (categ == categ_subcateg) and nivel != "Cualquiera":
            if num_preguntas <= adic.contar_preguntas(categ, subcateg, trad_nivel):
                mas_preguntas = True

        elif (categ == categ_subcateg) and nivel == "Cualquiera":
            if num_preguntas <= adic.contar_preguntas(categ, subcateg):
                mas_preguntas = True

        elif categ_larga != "Cualquiera" and subcateg_larga == "Cualquiera" and nivel != "Cualquiera":
            if num_preguntas <= adic.contar_preguntas(categ, nivel=trad_nivel):
                mas_preguntas = True

        elif categ_larga != "Cualquiera" and subcateg_larga == "Cualquiera" and nivel == "Cualquiera":
            if num_preguntas <= adic.contar_preguntas(categ):
                mas_preguntas = True

        elif categ_larga == "Cualquiera" and subcateg_larga == "Cualquiera" and nivel != "Cualquiera":
            if num_preguntas <= adic.contar_preguntas(nivel=trad_nivel):
                mas_preguntas = True

        elif categ_larga == "Cualquiera" and subcateg_larga == "Cualquiera" and nivel == "Cualquiera":
            if num_preguntas <= adic.contar_preguntas():
                mas_preguntas = True

        elif categ_larga == "Cualquiera" and subcateg_larga != "Cualquiera":
            messagebox.showerror("Error", "Si elige categoría 'Cualquiera', la subcategoría también deben ser 'Cualquiera")
            return
        else:
            messagebox.showerror("Error","Verifique que la categoría y subcategoría sean compatibles")
            return

        if mas_preguntas:
            if juego == "Selección-Múltiple":
                lista_preguntas_juegos = adic.obtener_preguntas_juego(num_preguntas, categ, subcateg, trad_nivel)
                orden_botones = adic.generar_orden_botones()
                adic.cambiar_frame(frame_show, frame_hide)
                seleccion_multiple("none")
                return
        else:
            messagebox.showerror("Error","No hay suficientes preguntas con esas características")

    boton_jugar = Button(frame6, text="Jugar", fg="black", bg="#70B824", font=("Arial",20), command = lambda:verificar_jugar(frame7, frame6))
    boton_jugar.config(cursor="hand2")
    boton_jugar.grid(row=5, column=1, pady=separy_F6)

    # Creando frame7 (Juego: Selección múltiple) -------------------------------------------------------------------------------------
    frame7 = Frame(raiz)
    frame7.config(width=ancho, height=alto, bg=color, cursor="arrow") 

    # Frame bien_mal
    bien_mal = Frame(raiz)
    frame7.config(width=ancho, height=alto, bg=color, cursor="arrow") 

    # Pregunta
    label_pregunta = Label(frame7, text="La pregunta es muy buen porque podría someter cualquier cosa", fg="black", bg="#D4A3FC", font=("Cooper Black",14), width=64, height=4)
    label_pregunta.grid(row=0, column=0, columnspan=2)

    # Creando "Buttons"
    boton_azul = Button(frame7, width=34, height=6, bg="#4DA3F0", fg="black", font=("Cooper Black",13), command = lambda:seleccion_multiple("azul"))
    boton_rojo = Button(frame7, width=34, height=6, bg="#EF5B5B", fg="black", font=("Cooper Black",13), command = lambda:seleccion_multiple("rojo"))
    boton_verde = Button(frame7, width=34, height=6, bg="#6DF04D", fg="black", font=("Cooper Black",13), command = lambda:seleccion_multiple("verde"))
    boton_amarillo = Button(frame7, width=34, height=6, bg="#F0E64D", fg="black", font=("Cooper Black",13), command = lambda:seleccion_multiple("amarillo"))

    def seleccion_multiple(color):
        """
        Ejecuta el juego de selección múltiple.
        :param str color: Color seleccionado.
        """
        global lista_preguntas_juegos
        global ronda
        global score_juego
        global orden_botones
        global inicia
        global act_user

        correcto = False

        pygame.mixer.music.stop()

        if color == "azul":
            time.sleep(1)
            if orden_botones[0] == 0:
                correcto = True
                score_juego += 1
            orden_botones = adic.generar_orden_botones()
            ronda += 1
            color = "none"

        elif color == "rojo":
            time.sleep(1)
            if orden_botones[1] == 0:
                correcto = True
                score_juego += 1
            orden_botones = adic.generar_orden_botones()
            ronda += 1
            color = "none"

        elif color == "verde":
            time.sleep(1)
            if orden_botones[2] == 0:
                correcto = True
                score_juego += 1
            orden_botones = adic.generar_orden_botones()
            ronda += 1
            color = "none"

        elif color == "amarillo":
            time.sleep(1)
            if orden_botones[3] == 0:
                correcto = True
                score_juego += 1
            orden_botones = adic.generar_orden_botones()
            ronda += 1
            color = "none"

        if inicia:
            if correcto:
                pygame.mixer.music.load("../recursor/sonidos/Correcto.wav")
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.load("../recursor/sonidos/Incorrecto.mp3")
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play()
        else:
            inicia = True
        time.sleep(2)

        if ronda > len(lista_preguntas_juegos):
            time.sleep(3)
            time.strftime
            messagebox.showinfo("Juego completado", "Tu puntaje ha sido de "+str(score_juego)+"/"+str(ronda-1))
            adic.actualzar_datos(usuarios, act_user, ronda-1, score_juego)
            ronda = 1
            lista_preguntas_juegos = []
            score_juego = 0 
            inicia = False
            adic.cambiar_frame(frame1, frame7)
            pygame.mixer.music.load("../recursor/sonidos/BonusLevel.mp3")
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(loops=-1)
            return

        label_pregunta.config(text="¿"+lista_preguntas_juegos[ronda-1][0]+"?")
        boton_azul.config(text=lista_preguntas_juegos[ronda-1][orden_botones[0]+1])
        boton_rojo.config(text=lista_preguntas_juegos[ronda-1][orden_botones[1]+1])
        boton_verde.config(text=lista_preguntas_juegos[ronda-1][orden_botones[2]+1])
        boton_amarillo.config(text=lista_preguntas_juegos[ronda-1][orden_botones[3]+1])
        score.config(text="Score: "+str(score_juego))

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

# Función main o principal
def main():
    """
    Función principal.
    """
    try:
        archivo = open("../recursor/archivos_quizmaker/preguntas_scrap.txt",'r')
        archivo.close()
    except:
        web.scrapear()
    arch.crear_archivos()
    crear_GUI()

# Ejecución de todo el programa
main()