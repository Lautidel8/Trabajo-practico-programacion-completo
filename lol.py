import tkinter as tk
from PIL import Image, ImageTk  # Importar Pillow para manipular imágenes

root = tk.Tk()

# Cargar la imagen usando PIL y redimensionarla
imagen = Image.open("C:\\Users\\lauti\\OneDrive\\Desktop\\programacion\\tp_gestion_autos\\trash-can.png")
imagen = imagen.resize((40, 40), Image.LANCZOS)  # Cambiar el tamaño a 40x40 píxeles
imagen = ImageTk.PhotoImage(imagen)

# Crear el botón con la imagen redimensionada
button = tk.Button(root, image=imagen)
button.place(x=200, y=200, height=41, width=41)

root.mainloop()
