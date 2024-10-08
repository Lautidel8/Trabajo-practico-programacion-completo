from interfaz import *

class Usuario:
    def __init__(self,nombre,constraseña,rol):
        self.nombre = nombre
        self.contraseña = constraseña
        self.rol = rol
        
def cargar_usuarios():
    usuarios = []
    try:
        with open("usuarios.bin", "rb") as archivo:
            while True:
                try:
                    usuario = pickle.load(archivo)
                    usuarios.append(usuario)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return usuarios

def registrar_usuario():
    indice_seleccionado = seleccion_admin_usuar.curselection()
    rol = seleccion_admin_usuar.get(indice_seleccionado)
    
    usuario_registrado = Usuario(entrada_nombre_usuario_registro.get(),entrada_constraseña_registro.get(), rol)
    
    with open("usuarios.bin","ab") as archivo:
        pickle.dump(usuario_registrado, archivo)

def verificar_usuario(archivo,nombre,contraseña):
    usuarios = cargar_usuarios() #llamo funcion para devolver la lista de objetos de Usuario
    for i in usuarios:
        if i.nombre == nombre and i.contraseña == contraseña and i.rol == "Administrador":
            return ingresar_a_pantalla_principal_administrador()
        
        elif i.nombre == nombre and i.contraseña == contraseña and i.rol == "Usuario":
            return print("ok2")
        
    return print("No existe")

def mostrar_usuarios():
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        print(f"Nombre: {usuario.nombre}, Contraseña: {usuario.contraseña}, Rol:{usuario.rol}")
        


