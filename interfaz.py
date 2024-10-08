
import tkinter as tk
import customtkinter as ctk 
from tkinter import messagebox,Frame
import pickle

from autos_Y_funciones import Auto,agregar_auto,cargar_autos_disponibles,modificar_auto,cargar_lista_autos,eliminar_auto,mostrar_autos_disponibles
from usuarios_Y_funciones import Usuario,mostrar_usuarios,verificar_usuario,registrar_usuario,cargar_usuarios


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
    
    cargar_lista_autos()

def volver_a_inicio_admin():
    pantalla_modificar_autos.pack_forget()
    pantalla_princial_admin.pack(expand=True, fill="both")


# Crear una instancia de la clase Tk
inicio = tk.Tk()
inicio.geometry("720x480")
inicio.title("SISTEMA GESTOR DE VEHICULOS")


#INICIO
login = tk.Frame(inicio)
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

boton = tk.Button(login, text = "Todavia no tengo usuario", command = ir_a_registro)
boton.place(x=340, y=300, height=40, width=150)

boton_mostrar_usuarios = tk.Button(login, text = "Mostrar usuarios", command = mostrar_usuarios)
boton_mostrar_usuarios.place(x=140, y=300, height=40, width=150)

boton_inicio_Sesion = tk.Button(login, text = "Iniciar Sesion", command =lambda: verificar_usuario("usuarios.bin", entrada_nombre_usuario.get(), entrada_constraseña.get()))
boton_inicio_Sesion.place(x=500, y=300, height=40, width=150)

#REGISTRO
registro = tk.Frame(inicio)

boton1 = tk.Button(registro, text = "volver a menu", command = volver_a_inicio)
boton1.place(x=140, y=300, height=40, width=150)

entrada_nombre_usuario_registro = tk.Entry(registro)
entrada_nombre_usuario_registro.place(x=300, y=100, height=40, width=200 )

entrada_constraseña_registro = tk.Entry(registro)
entrada_constraseña_registro.place(x=300, y=150, height=40, width=200 )

boton_registro = tk.Button(registro, text = "registrarse", command = registrar_usuario)
boton_registro.place(x=340, y=300, height=40, width=150)

seleccion_admin_usuar = tk.Listbox(registro)
seleccion_admin_usuar.place(x=300, y=200, height=40, width=100)
seleccion_admin_usuar.insert(1,"Administrador")
seleccion_admin_usuar.insert(2,"Usuario")

#PANTALLA PRINCIPAL ADMNISTRADOR
pantalla_princial_admin = tk.Frame(inicio)

boton_agregar_auto = tk.Button(pantalla_princial_admin, text = "Agregar automovil", command = ingresar_a_pantalla_agregar)
boton_agregar_auto.place(x=440, y=300, height=40, width=150)

boton_modificar_auto = tk.Button(pantalla_princial_admin, text = "Modificar Automovil o Eliminar Automovil", command = ingresar_pantalla_modificar)
boton_modificar_auto.place(x=100, y=300, height=40, width=250)


#PANTALLA AGREGAR AUTO
pantalla_agregar_autos = tk.Frame(inicio)

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

boton_confirm_agregar_auto = tk.Button(pantalla_agregar_autos, text = "Confirmar", command = agregar_auto)
boton_confirm_agregar_auto.place(x=300, y=300, height=40, width=150)

boton_mostrar_autos = tk.Button(pantalla_agregar_autos, text = "Mostrar autos disponibles", command = mostrar_autos_disponibles)
boton_mostrar_autos.place(x=140, y=300, height=40, width=150)

#PANTALLA MODIFICAR AUTO

pantalla_modificar_autos = tk.Frame(inicio)

lista_autos = tk.Listbox(pantalla_modificar_autos)
lista_autos.place(x=300, y=100, height=100, width=200)

boton_eliminar_auto = tk.Button(pantalla_modificar_autos, text = "Eliminar automovil", command = eliminar_auto)
boton_eliminar_auto.place(x=500, y=300, height=40, width=150)

boton_modificar_auto = tk.Button(pantalla_modificar_autos, text="Modificar auto", command=modificar_auto)
boton_modificar_auto.place(x=200, y=300, height=40, width=150)

boton_volver = tk.Button(pantalla_modificar_autos, text="Volver", command= volver_a_inicio_admin)
boton_volver.place(x=350, y=300, height=40, width=150)

inicio.mainloop()
