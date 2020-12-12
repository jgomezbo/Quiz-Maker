import archivos as arch

def registro_usuario(usuario, contraseña, usuarios):
    '''
    Agrega al usuario que se está resgitrando al diccionario donde se encuentran los demás usuarios.
    :param str usuario: nombre que elije el usuario.
    :param str contraseña: contraseña que elije el usuario.
    :param dict usuarios: diccionario de usuarios.
    :return: True|False
    '''
    if usuario not in usuarios:
        usuarios[usuario]=[contraseña,"0/0",0,0]
        return True
    return False
    
def datos_usuario(usuario, punt_max, t_partidas, partidas_won, usuarios):
    '''
    Almacena en el diccionario de usuarios los nuevos datos del usuario especificado.
    :param str usuario: usuario específico al que se le almacenarán las estadísticas de juego.
    :param str punt_max: puntaje máximo obtenido por el usuario.
    :param int t_partidas: Total rondas jugadas.
    :param int partidas_won: rondas ganadas por el jugador.
    :param dict usuarios: diccionario de usuarios.
    '''
    usuarios[usuario][1]=punt_max
    usuarios[usuario][2]=t_partidas
    usuarios[usuario][3]=partidas_won

    almacenar_usuarios(usuarios)

def almacenar_usuarios(usuarios):
    '''
    Almacena a los usuarios que se encuentran en el diccionario 
    de usuarios en un archivo, sin embargo primero limpia el archivo.
    :param dict usuarios: diccionario de usuarios.
    '''
    limpiar()
    for dato in usuarios:
        usuario = dato
        contraseña = usuarios[dato][0]
        punt_max = usuarios[dato][1]
        p_ganadas = usuarios[dato][2]
        p_perdidas = usuarios[dato][3]
        vacio = arch.is_archivo_vacio('Usuarios.txt')
        if vacio:
            user=usuario+'^'+contraseña+'^'+punt_max+'^'+str(p_ganadas)+'^'+str(p_perdidas)
        else:
            user='^'+'\n'+usuario+'^'+contraseña+'^'+punt_max+'^'+str(p_ganadas)+'^'+str(p_perdidas)
        archivo=open('../recursor/archivos_quizmaker/Usuarios.txt','a')
        archivo.write(user)
        archivo.close()

def comprobar_usuario(usuario, contraseña, usuarios):
    '''
    Comprueba si el usuario y contraseña ingresados son correctos.
    :param string usuario: usuario ingresado.
    :param string contraseña: contraseña ingresada.
    :param dict usuarios: diccionario de usuarios.
    return: bool, int
    '''
    valido=0
    usuario_incorrecto=False
    contraseña_incorrecta=False
    if usuario in usuarios:
        valido+=1
        if contraseña==usuarios[usuario][0]:
            valido+=1
        else:
            contraseña_incorrecta=True
    else:
        usuario_incorrecto=True
    if valido==2:
        return True,0
    elif usuario_incorrecto:
        return False,1
    elif contraseña_incorrecta:
        return False,2

def archivo_a_diccionario(usuarios):
    '''
    En el diccionario existente, agrega los usuarios que se encuentran en un archivo de texto.
    :param dict usuarios: diccionario de usuarios.
    '''
    users=arch.leer_archivo('Usuarios.txt')
    for renglon in range(len(users)):
        user=users[renglon]
        userl=user.split('^')
        usuario=userl[0]
        contraseña=userl[1]
        p_max=userl[2]
        p_ganadas=userl[3]
        p_perdidas=userl[4]
        usuarios[usuario]=[contraseña,p_max,p_ganadas,p_perdidas]

def limpiar():
    '''
    Limpia el archivo de los viejos usuarios.
    '''
    archivo=open('../recursor/archivos_quizmaker/Usuarios.txt','w')
    archivo.close()