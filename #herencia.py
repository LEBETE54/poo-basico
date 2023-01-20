#herencia
#super clase cual quier metodo o atributo lo heredara su clase hija
class Usuarios:
    tipo_usuario= "free"
    publicidad= True
    
    def __init__(self,id,alias,nombre):
        self.id=id
        self.alias=alias
        self.nombre=nombre
    def muestra_datos(self):
        print("el nombre e iddel usuario es: " +self.nombre,self.id)
        print("el alias del usuario es: "+self.alias)
   
    #colocando los parentesis y el nombre de la clase de la cual quieres heredar (esto es algo uni lateral solo la que hereda recibe nueva info)
class Usuarios_premium(Usuarios):
    tipo_usuario= "prmium"
    publicidad= False
    #con esto nos podemos ahorra lineas de codigo in necesarias esto se vuelve muy util con clases de mayor tamaño
    """def __init__(self,id,alias,nombre):
        self.id=id
        self.alias=alias
        self.nombre=nombre
    def muestra_datos(self):
        print("el nombre e iddel usuario es: " +self.nombre,self.id)
        print("el alias del usuario es: "+self.alias)"""

#aqui nuevamente especificamos los datos del init
usuario01=Usuarios("011","alekei","alejandro")
usuario02=Usuarios_premium("012","miri","miranda s")

usuario02.muestra_datos

