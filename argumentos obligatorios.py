""" diferencia entre atributos especificados fueras del __init__ y los peretenecientes a este, los atributos  del metod init sirven para darle un 
valor inicial a los atributos de un objeto esto no significa que no se puedan agregar mas tributos lo que implica el init esque tendras que usar 
los argumentos que tengas dentro del metodo init de forma obligatoria
"""
#usemos este de ejemplo
class Usuarios:
    tipo_usuario= "free"
    publicidad= True
    
    def __init__(self,id,alias,nombre):
        self.id=id
        self.alias=alias
        self.nombre=nombre
    #aqui como ya sabemos el metodo init nos permite a nosostros asignarle un valor inicial a los atributos que pusimo en el init
    #y no es necesario especificar los otros dos argumentos
    
usuario01=Usuarios("055","lebete","alejandro")
#aqui se imprime al atributo de publicidad y como se puede ver no esta especificado en el metodo init

print(usuario01.publicidad)

print(usuario01.alias,usuario01.id)