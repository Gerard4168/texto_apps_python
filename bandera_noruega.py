#se importa la libreria de tkinter con todas sus funciones 
from tkinter import *


#.....................
# funciones de la app
#.....................


#.....................
# ventana principal
#.....................

# se declara una variable llamada ventana principal, que adquiere las caracteristicas de un objeto Tk ()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Bandera NORUEGA")

# tamaño de la ventana
ventana_principal.geometry("600x400")

# deshabilitar boton de minimizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg="red")

#----------------------------
# frame entrada datos
# ----------------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white" , width=600, height=90)
frame_entrada.place(x=0, y=200)

frame_entrada2 = Frame(ventana_principal)
frame_entrada2.config(bg="white" , width=80, height=600)
frame_entrada2.place(x=140, y=0)

#----------------------------
# frame operaciones
# ----------------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="blue" , width=600, height=70)
frame_operaciones.place(x=0, y=210)

frame_operaciones2 = Frame(ventana_principal)
frame_operaciones2.config(bg="blue" , width=60, height=600)
frame_operaciones2.place(x=150, y=0)




# run
# se ejecuta la funcion (metodo) mainloop()de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el usuario haga. Cada accion del usuario se conoce como evento. El mainloop() es un bucle infinito.
ventana_principal.mainloop()