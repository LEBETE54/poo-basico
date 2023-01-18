class NombreClase:
    pass
#al crear el objeto y asignarlo a una clase este obtiene todos los tributos que se estblecen en ella

primer_objeto= Nombre

#atributos=prpiedades =variables u otros objetos

class NinjaPrincipal:
   #se ponen los tributos 
    HP=100
    resistencia=50
    xp=1
    #metodo es una funcion
    def game_over(self):
        print("game over")

#se asigna el objeto a la clase
ninja =NinjaPrincipal
#se llama al tributos usando el nombre del objeto . nombre del atributo
print(ninja.HP)
#aqui relacionamos un atributo a un metodo   
if ninja.HP ==0:
    ninja.game_over