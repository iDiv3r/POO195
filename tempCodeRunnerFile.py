txtEdad.get())
    
    validacion = controlador.verificarEdadCont(edad)
    
    if validacion == 1:
        lblVerif.config(text="Eres Mayor de edad",bg="green")
    else:
        lblVerif.config(text="Eres Menor de edad",bg="red")
    

def buscarUsuario():
    nombre = txtNombre.get()
    
    busqueda = controlador.buscarNombre(nombre)
    
    if busqueda == 1:
        lblBusq.config(text="Usuario Encontrado",bg="green")
    else: