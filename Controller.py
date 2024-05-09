class ExcepcionEdadInvalida(Exception):
    def __init__(self, edad, mensaje="La edad ingresada es menor a 18"):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ExcepcionNombre(Exception):
    "Ocurre cuando no se encuentra el nombre en la lista"
    pass


class Controller:
    
    lista = ["emiliano"]

    def verificarEdadCont(self,edad):
        
        if edad < 18:
            raise ExcepcionEdadInvalida(edad)
        else:
            return 1
        
    
    
    def buscarNombre(self,nombre):
        try:
            if nombre in self.lista:
                return 1
            else:
                raise ExcepcionNombre
            
        except ExcepcionNombre:
            print("Error, el nombre no se encontró")
