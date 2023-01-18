#atributos obligatorios

class Alumnos:
    def __init__(self, nombre ,apellidos, cursos,Materias):
        self.nombre = nombre
        self.apellidos= apellidos
        self.cursos = cursos
        self.Materias=Materias
#en este cso despues de usar el metodo init tenemos que especificar el valor de las variables en orden sucesivo despues del self
#nombre ]= lucia  apellidos =roma curso=fisico
alumno001=Alumnos("lucia","roma","fisico","estructuras")
print(alumno001.cursos)
#asi cada que se cree un objeto nuevo con el metodo init se puede eficientar y acortar el trabajo a la hora de asignar atributos
print(alumno001.cursos,alumno001.nombre)

 

#en el segundo objeto el parametro Materias lo ponemos como lista para asi agregar multplies atributos

alumno002=Alumnos("carlos","perez","sistemas",["ingles","poo"])

print(alumno002.Materias)

 #igual utilizando append se puedern agregar mas elementos
 alumno002.Materias.append("matematicas")