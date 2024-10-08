
from interfaz import *

class Auto:
    def __init__(self,marca, modelo, año, precio_por_día, disponibilidad):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_por_dia = precio_por_día
        self.disponib = disponibilidad

#FUNCIONES DE INTANCIA DE CLASES Y CARGA EN ARCHIVOS
def agregar_auto():
    
    autos_disponibles = cargar_autos_disponibles()
    
    auto_agregado = Auto(entrada_marca.get(),entrada_modelo.get(), entrada_año.get(), entrada_precio_por_dia.get(), True)
    
    autos_disponibles.append(auto_agregado)
        
    with open("autos_disponibles.bin", "wb") as file:
            pickle.dump(autos_disponibles, file)
            
def cargar_autos_disponibles():
    try:
        with open("autos_disponibles.bin", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    
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

    cargar_lista_autos()

    messagebox.showinfo("Éxito", "Los cambios han sido guardados correctamente.")

def cargar_lista_autos():
    lista_autos.delete(0, tk.END)  # Limpiar la lista primero
    autos_disponibles = cargar_autos_disponibles()
    for i, auto in enumerate(autos_disponibles):
        lista_autos.insert(i, f"{auto.marca} {auto.modelo} ({auto.año})")

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

def mostrar_autos_disponibles():
    autos = cargar_autos_disponibles()
    for i in autos:
        print(f"marca: {i.marca}, modelo: {i.modelo}, año:{i.año},precio:{i.precio_por_dia}")