#encapsuslamiento
"""es un principio de diseño que se refiere a la ocultación de detalles de implementación de una clase,
módulo o sistema para proteger su integridad y permitir que solo ciertos aspectos sean accesibles 
o modificables por otras partes del programa. Esto se logra mediante el uso de modificadores de acceso,
como "public", "private" y "protected". El encapsulamiento ayuda a aumentar la seguridad, la fiabilidad 
y la reutilizabilidad del código."""
class Usuarios:
    tipo_usuario= "free"
    publicidad= True
    
    def __init__(self,id,alias,nombre,password):
        self.id=id
        self.alias=alias
        self.nombre=nombre
    
        
        self.__password=password 
        # self.password=password 
    def muestra_datos(self):
        print("el nombre e iddel usuario es: " +self.nombre,self.id)
        print("el alias del usuario es: "+self.alias)


usuario001=Usuarios("001","alekei","alejandro p","pollitoamarillo")

usuario001.muestra_datos