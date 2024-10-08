import tkinter as tk
import customtkinter as ctk 
from tkinter import messagebox,Frame
import pickle
from PIL import Image, ImageTk

class Usuario:
    def __init__(self,nombre,constraseña,rol):
        self.nombre = nombre
        self.contraseña = constraseña
        self.rol = rol
        self.autos_reservados = []
      
class Auto:
    def __init__(self,marca, modelo, año, precio_por_día, disponibilidad=True):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_por_dia = precio_por_día
        self.disponib = disponibilidad


usuario_logueado = None

#FUNCIONES DE INTANCIA DE CLASES Y CARGA EN ARCHIVOS
def agregar_auto():
    
    autos_disponibles = cargar_autos_disponibles()
    
    auto_agregado = Auto(entrada_marca.get(),entrada_modelo.get(), entrada_año.get(), entrada_precio_por_dia.get(), True)
    
    autos_disponibles.append(auto_agregado)
        
    with open("autos_disponibles.bin", "wb") as file:
            pickle.dump(autos_disponibles, file)
            
    pantalla_agregar_autos.pack_forget()
    pantalla_princial_admin.pack(expand=True, fill="both")
    
def cargar_autos_disponibles():
    try:
        with open("autos_disponibles.bin", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def registrar_usuario():
    indice_seleccionado = seleccion_admin_usuar.curselection()
    rol = seleccion_admin_usuar.get(indice_seleccionado)
    
    usuario_registrado = Usuario(entrada_nombre_usuario_registro.get(),entrada_constraseña_registro.get(), rol)
    
    with open("usuarios.bin","ab") as archivo:
        pickle.dump(usuario_registrado, archivo)

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

def cargar_lista_usuarios():
    lista_usuarios.delete(0, tk.END)
    usuarios_disponibles = cargar_usuarios()
    for i, j in enumerate(usuarios_disponibles):
        lista_usuarios.insert(i, f"{j.nombre} {j.contraseña} ({j.rol})")
        
def mostrar_usuarios():
    cargar_lista_usuarios()
    lista_usuarios.place(x=250, y=100, height=150, width=190)
    boton_borrar_usuario.place(x=450, y=100, height=50, width=50)
    
    

#FUNCIONES DE CAMBIO DE PANTALLA
def ir_a_registro():
    login.pack_forget()  # Ocultar el frame de inicio de sesión
    registro.pack(expand=True,fill="both")  # Mostrar el frame de registro
    
def volver_a_inicio():
    registro.pack_forget()
    login.pack(expand=True, fill="both")

def ingresar_a_pantalla_principal_administrador():
    login.pack_forget()
    pantalla_princial_admin.pack(expand=True,fill="both")

def ingresar_a_pantalla_agregar():
    pantalla_princial_admin.pack_forget()
    pantalla_agregar_autos.pack(expand=True,fill="both")

def ingresar_pantalla_modificar():
    pantalla_princial_admin.pack_forget()
    pantalla_modificar_autos.pack(expand=True,fill="both")
    
    cargar_lista_autos(lista_autos)

def volver_a_inicio_admin():
    pantalla_modificar_autos.pack_forget()
    pantalla_princial_admin.pack(expand=True, fill="both")

def ingresar_pantalla_principal_usuario():
    login.pack_forget()
    pantalla_principal_usuario.pack(expand=True,fill="both")

#FUNCIONES MODIFICACION
def modificar_auto():
    def ventana_secu():
        ventana_secundaria_mod = tk.Toplevel(pantalla_modificar_autos)
        ventana_secundaria_mod.title("Modificar autos")
        ventana_secundaria_mod.geometry("300x200")

        entrada_marca2 = tk.Entry(ventana_secundaria_mod)
        entrada_marca2.pack()
        entrada_marca2.insert(0, auto_seleccionado.marca)

        entrada_modelo2 = tk.Entry(ventana_secundaria_mod)
        entrada_modelo2.pack()
        entrada_modelo2.insert(0, auto_seleccionado.modelo)

        entrada_año2 = tk.Entry(ventana_secundaria_mod)
        entrada_año2.pack()
        entrada_año2.insert(0, auto_seleccionado.año)
        
        entrada_precio_por_dia2 = tk.Entry(ventana_secundaria_mod)
        entrada_precio_por_dia2.pack()
        entrada_precio_por_dia2.insert(0, auto_seleccionado.precio_por_dia)

        cartel_marca_mod = tk.Label(ventana_secundaria_mod, text="Marca")
        cartel_marca_mod.place(x=40, y=1)
        
        cartel_modelo_mod = tk.Label(ventana_secundaria_mod, text="Modelo")
        cartel_modelo_mod.place(x=40, y=16)

        cartel_año_mod = tk.Label(ventana_secundaria_mod, text="Año")
        cartel_año_mod.place(x=40, y=35)

        cartel_precioXdia_mod = tk.Label(ventana_secundaria_mod, text="Precio por día")
        cartel_precioXdia_mod.place(x=10, y=55)
        
        boton_guardar_cambios = tk.Button(ventana_secundaria_mod, text="Guardar cambios", 
                                          command=lambda: guardar_cambios_auto(selected_index[0], entrada_marca2.get(), 
                                                                               entrada_modelo2.get(), entrada_año2.get(), 
                                                                               entrada_precio_por_dia2.get()))
        boton_guardar_cambios.place(x=50, y=100)


    autos_disponibles_para_mod = cargar_autos_disponibles()


    selected_index = lista_autos.curselection()
    
    if selected_index:
        auto_seleccionado = autos_disponibles_para_mod[selected_index[0]]
        ventana_secu()
    else:
        messagebox.showerror("Error", "Por favor selecciona un auto para modificar.")

def guardar_cambios_auto(selected_index, nueva_marca, nuevo_modelo, nuevo_año, nuevo_precio):
    
    if not nueva_marca or not nuevo_modelo or not nuevo_año or not nuevo_precio:
        messagebox.showerror("Error", "Todos los campos deben estar completos.")
        return

    try:
        nuevo_año = int(nuevo_año)  # Asegurarse de que el año sea un número
        nuevo_precio = float(nuevo_precio)  # Asegurarse de que el precio sea un número
    except ValueError:
        messagebox.showerror("Error", "El año y el precio deben ser valores numéricos.")
        return

    autos_disponibles = cargar_autos_disponibles()

    autos_disponibles[selected_index].marca = nueva_marca
    autos_disponibles[selected_index].modelo = nuevo_modelo
    autos_disponibles[selected_index].año = nuevo_año
    autos_disponibles[selected_index].precio_por_dia = nuevo_precio

    with open("autos_disponibles.bin", "wb") as file:
        pickle.dump(autos_disponibles, file)

    cargar_lista_autos(lista_autos)

    messagebox.showinfo("Éxito", "Los cambios han sido guardados correctamente.")

def cargar_lista_autos(list_box):
    list_box.delete(0, tk.END)  # Limpiar la lista primero
    autos_disponibles = cargar_autos_disponibles()
    for i, auto in enumerate(autos_disponibles):
        list_box.insert(i, f"{auto.marca} {auto.modelo} ({auto.año})  ${auto.precio_por_dia})")

#FUNCION ELIMINAR
def eliminar_auto():
    selected_index = lista_autos.curselection()
    
    if selected_index:
        confirmar = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este auto?")
        
        if confirmar:
            autos_disponibles = cargar_autos_disponibles()

            del autos_disponibles[selected_index[0]]

            with open("autos_disponibles.bin", "wb") as file:
                pickle.dump(autos_disponibles, file)

            cargar_lista_autos()

            messagebox.showinfo("Éxito", "El auto ha sido eliminado correctamente.")
    else:
        messagebox.showerror("Error", "Por favor selecciona un auto para eliminar.")

def eliminar_usuario():

    usuario_selecc_para_eliminar = lista_usuarios.curselection()

    if usuario_selecc_para_eliminar:
        confirm = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este usuario?")
        
        if confirm:
            usuarios_disponibles = cargar_usuarios()  # Carga todos los usuarios
            
            # Eliminar el usuario seleccionado
            del usuarios_disponibles[usuario_selecc_para_eliminar[0]]
            
            # Guardar la lista actualizada de usuarios (sobreescribiendo el archivo correctamente)
            with open("usuarios.bin", "wb") as file:
                for usuario in usuarios_disponibles:
                    pickle.dump(usuario, file)
            
            cargar_lista_usuarios()  # Recargar la lista en la interfaz
            
            messagebox.showinfo("Éxito", "El usuario ha sido eliminado correctamente.")
    
    else:
        messagebox.showerror("Error", "Por favor, seleccione un usuario para eliminar.")



def ver_detalle():
    
    autos_disponibles_para_detalles = cargar_autos_disponibles()
    selected_index = lista_autos_para_reservar.curselection()
    
    if selected_index:
        auto_seleccionado = autos_disponibles_para_detalles[selected_index[0]]
        
        ventana_secundaria_det = tk.Toplevel(pantalla_principal_usuario)
        ventana_secundaria_det.title("Detalles")
        ventana_secundaria_det.geometry("300x200")
        
        cartel_marca_det = tk.Label(ventana_secundaria_det, text = auto_seleccionado.marca)
        cartel_marca_det.place(x=100, y=50)
        
        cartel_marca_nombre = tk.Label(ventana_secundaria_det, text = "marca:",relief=tk.FLAT, fg="white", bg="steel blue")
        cartel_marca_nombre.place(x=50, y=50)
            
        cartel_modelo_det = tk.Label(ventana_secundaria_det, text=auto_seleccionado.modelo)
        cartel_modelo_det.place(x=100, y=90)
        
        cartel_modelo_nombre = tk.Label(ventana_secundaria_det, text = "modelo:",relief=tk.FLAT, fg="white", bg="steel blue")
        cartel_modelo_nombre.place(x=50, y=90)

        cartel_año_det = tk.Label(ventana_secundaria_det, text=auto_seleccionado.año)
        cartel_año_det.place(x=100, y=130)
        
        cartel_año_nombre = tk.Label(ventana_secundaria_det, text = "año:",relief=tk.FLAT, fg="white", bg="steel blue")
        cartel_año_nombre.place(x=50, y=130)

        cartel_precioXdia_det = tk.Label(ventana_secundaria_det, text=auto_seleccionado.precio_por_dia)
        cartel_precioXdia_det.place(x=100, y=170)
        
        cartel_precio_nombre = tk.Label(ventana_secundaria_det, text = "precio por dia:",relief=tk.FLAT, fg="white", bg="steel blue")
        cartel_precio_nombre.place(x=10, y=170)
            
        boton_reservar_auto = tk.Button(ventana_secundaria_det, text="Reservar",relief=tk.SOLID, fg="white", bg="steel blue",command=lambda: reservar_auto(auto_seleccionado, ventana_secundaria_det))
        boton_reservar_auto.place(x=200,y=100,height=25,width=90)
            
    else:
        messagebox.showerror("Error", "Por favor selecciona un auto para ver detalle.")
    
def reservar_auto(auto_seleccionado, ventana_detalle):
    
    usuarios = cargar_usuarios()
    usuario_actual = obtener_usuario_actual()

    if auto_seleccionado.disponib == True:
        
        auto_seleccionado.disponib = False
        usuario_actual.autos_reservados.append(auto_seleccionado)
        autos_disponibles = cargar_autos_disponibles()
        
        for i in autos_disponibles:
            if i.marca == auto_seleccionado.marca and i.modelo == auto_seleccionado.modelo and i.año == auto_seleccionado.año:
                i.disponib = False
        
        
        with open("autos_disponibles.bin", "wb") as file:
            pickle.dump(autos_disponibles, file)

        with open("usuarios.bin", "wb") as file:
            for usuario in usuarios:
                pickle.dump(usuario, file)

        ventana_detalle.destroy()
        messagebox.showinfo("Éxito", "Auto reservado correctamente.")
    else:
        messagebox.showerror("Error", "Este auto ya está reservado.")


def obtener_usuario_actual():
    return usuario_logueado

def verificar_usuario(archivo, nombre, contraseña):
    #al declarar una variable como global dentro de una función, estás indicando que deseas usar la variable global
    #en lugar de crear una nueva variable local con el mismo nombre
    
    global usuario_logueado
    usuarios = cargar_usuarios()
    
    for usuario in usuarios:
        if usuario.nombre == nombre and usuario.contraseña == contraseña:
            usuario_logueado = usuario
            
            if usuario.rol == "Administrador":
                ingresar_a_pantalla_principal_administrador()
            elif usuario.rol == "Usuario":
                ingresar_pantalla_principal_usuario()
                cargar_lista_autos(lista_autos_para_reservar)
            return
        
    messagebox.showerror("Incorrecto", "El usuario ingresado no es válido")


# Crear una instancia de la clase Tk
inicio = tk.Tk()
inicio.geometry("720x480")
inicio.title("SISTEMA GESTOR DE VEHICULOS")


#INICIO
login = tk.Frame(inicio,bg="gainsboro")
login.pack(expand=True,fill="both")

cartel_usuario = tk.Label(inicio,text="Usuario")
cartel_usuario.place(x=200,y=110,height=20,width=100)

cartel_contra = tk.Label(inicio,text="Contraseña")
cartel_contra.place(x=200,y=160,height=20,width=100)

entrada_nombre_usuario = tk.Entry(login)
entrada_nombre_usuario.place(x=300, y=100, height=40, width=200 )
nombre_usuario_verificar = entrada_nombre_usuario.get()

entrada_constraseña = tk.Entry(login)
entrada_constraseña.place(x=300, y=150, height=40, width=200 )
contraseña_verificar = entrada_constraseña.get()

boton = tk.Button(login, text = "Todavia no tengo usuario",relief=tk.FLAT, fg="white", bg="steel blue", command = ir_a_registro)
boton.place(x=200, y=300, height=40, width=150)

boton_inicio_Sesion = tk.Button(login, text = "Iniciar Sesion",relief=tk.FLAT, fg="white", bg="steel blue", command =lambda: verificar_usuario("usuarios.bin", entrada_nombre_usuario.get(), entrada_constraseña.get()))
boton_inicio_Sesion.place(x=400, y=300, height=40, width=150)



#REGISTRO
registro = tk.Frame(inicio,bg="gainsboro")

boton1 = tk.Button(registro, text = "volver a menu",relief=tk.FLAT, fg="white", bg="steel blue", command = volver_a_inicio)
boton1.place(x=140, y=300, height=40, width=150)

entrada_nombre_usuario_registro = tk.Entry(registro)
entrada_nombre_usuario_registro.place(x=300, y=100, height=40, width=200 )

entrada_constraseña_registro = tk.Entry(registro)
entrada_constraseña_registro.place(x=300, y=150, height=40, width=200 )

boton_registro = tk.Button(registro, text = "registrarse",relief=tk.FLAT, fg="white", bg="steel blue", command = registrar_usuario)
boton_registro.place(x=340, y=300, height=40, width=150)

cartel_usuario2 = tk.Label(registro,text="Usuario")
cartel_usuario2.place(x=200,y=110,height=20,width=100)

cartel_contra2 = tk.Label(registro,text="Contraseña")
cartel_contra2.place(x=200,y=160,height=20,width=100)

cartel_adminOusu = tk.Label(registro,text="Seleccione su rol")
cartel_adminOusu.place(x=200,y=210,height=20,width=100)

seleccion_admin_usuar = tk.Listbox(registro)
seleccion_admin_usuar.place(x=300, y=200, height=40, width=100)
seleccion_admin_usuar.insert(1,"Administrador")
seleccion_admin_usuar.insert(2,"Usuario")

#--------------------------------------------------------------------------------------------------------

#PANTALLA PRINCIPAL ADMNISTRADOR
pantalla_princial_admin = tk.Frame(inicio,bg="gainsboro")

boton_agregar_auto = tk.Button(pantalla_princial_admin, text = "Agregar automovil",relief=tk.FLAT, fg="white", bg="steel blue", command = ingresar_a_pantalla_agregar)
boton_agregar_auto.place(x=440, y=300, height=40, width=150)

boton_modificar_auto = tk.Button(pantalla_princial_admin, text = "Modificar Automovil o Eliminar Automovil",relief=tk.FLAT, fg="white", bg="steel blue", command = ingresar_pantalla_modificar)
boton_modificar_auto.place(x=100, y=300, height=40, width=250)

boton_mostrar_usuarios = tk.Button(pantalla_princial_admin, text = "Mostrar usuarios",relief=tk.FLAT, fg="white", bg="steel blue", command = mostrar_usuarios)
boton_mostrar_usuarios.place(x=300, y=360, height=40, width=150)


lista_usuarios = tk.Listbox(pantalla_princial_admin)

imagen_trash = Image.open("C:\\Users\\lauti\\OneDrive\\Desktop\\programacion\\tp_gestion_autos\\trash-can.png")
imagen_trash = imagen_trash.resize((40, 40), Image.LANCZOS)
imagen_trash = ImageTk.PhotoImage(imagen_trash)

boton_borrar_usuario = tk.Button(pantalla_princial_admin, image=imagen_trash,relief=tk.SOLID, bg="red3", command = eliminar_usuario)


#PANTALLA AGREGAR AUTO
pantalla_agregar_autos = tk.Frame(inicio,bg="gainsboro")

entrada_marca = tk.Entry(pantalla_agregar_autos)
entrada_marca.place(x=300, y=100, height=40, width=200 )

entrada_modelo = tk.Entry(pantalla_agregar_autos)
entrada_modelo.place(x=300, y=150, height=40, width=200 )

entrada_año = tk.Entry(pantalla_agregar_autos)
entrada_año.place(x=300, y=200, height=40, width=200 )

entrada_precio_por_dia = tk.Entry(pantalla_agregar_autos)
entrada_precio_por_dia.place(x=300, y=250, height=40, width=200 )

cartel_marca = tk.Label(pantalla_agregar_autos,text="Marca")
cartel_marca.place(x=200,y=110,height=20,width=100)

cartel_modelo = tk.Label(pantalla_agregar_autos,text="Modelo")
cartel_modelo.place(x=200,y=160,height=20,width=100)

cartel_año = tk.Label(pantalla_agregar_autos,text="Año")
cartel_año.place(x=200,y=210,height=20,width=100)

cartel_precioXdia = tk.Label(pantalla_agregar_autos,text="Precio por dia")
cartel_precioXdia.place(x=200,y=260,height=20,width=100)

boton_confirm_agregar_auto = tk.Button(pantalla_agregar_autos, text = "Confirmar",relief=tk.FLAT, fg="white", bg="steel blue", command = agregar_auto)
boton_confirm_agregar_auto.place(x=300, y=300, height=40, width=150)


#PANTALLA MODIFICAR AUTO

pantalla_modificar_autos = tk.Frame(inicio,bg="gainsboro")

lista_autos = tk.Listbox(pantalla_modificar_autos)
lista_autos.place(x=300, y=100, height=100, width=200)

boton_eliminar_auto = tk.Button(pantalla_modificar_autos, text = "Eliminar automovil",relief=tk.FLAT, fg="white", bg="steel blue", command = eliminar_auto)
boton_eliminar_auto.place(x=550, y=300, height=40, width=150)

boton_modificar_auto = tk.Button(pantalla_modificar_autos, text="Modificar auto",relief=tk.FLAT, fg="white", bg="steel blue", command=modificar_auto)
boton_modificar_auto.place(x=150, y=300, height=40, width=150)

boton_volver = tk.Button(pantalla_modificar_autos, text="Volver",relief=tk.FLAT, fg="white", bg="steel blue", command= volver_a_inicio_admin)
boton_volver.place(x=350, y=300, height=40, width=150)

#--------------------------------------------------------------------------------------------------------------------------------

#PANTALLA PRINCIPAL USUARIOS

pantalla_principal_usuario = tk.Frame(inicio,bg="gainsboro")


lista_autos_para_reservar = tk.Listbox(pantalla_principal_usuario)
lista_autos_para_reservar.place(x=200, y=100, height=200, width=400)

boton_ver_detalle = tk.Button(pantalla_principal_usuario, text="Ver detalle",relief=tk.FLAT, fg="white", bg="steel blue", command = ver_detalle)
boton_ver_detalle.place(x=200, y=300, height=40, width=150)


inicio.mainloop()
