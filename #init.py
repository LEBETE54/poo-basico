#init
class NinjaPrincipal:
   #se pone junto con el self todos los atributos del metodo
   #aqui en lugar de asignar un valor especifico a la variable se le asigna la variable en si para que al llamarlo en tro objeto se le pueda asignar valores diferentes
   
   def __init__ (self, HP,resistencia,xp):
   #se ponen los tributos 
    self.HP=HP
    self.resistencia= resistencia
    xp=xp
    #metodo es una funcion
    def game_over(self):
        print("game over")
#aqui al asiganar la clase se tendran que asignar los valres en el mismo orden 
#con el que se pusieron en el self, HP=25 ,resistencia=10,xp = 1
#con esto reducimos la cantidad de lneas necesarias
#compara  

ninja_enemigo=NinjaPrincipal(25,10,1)
ninja_principal=NinjaPrincipal(100,50,1)
#se asigna el objeto a la clase
#en estre ejemplo se utilizan lineas no necesareas pero validas
""""ninja =NinjaPrincipal
#se llama al tributos usando el nombre del objeto . nombre del atributo
print(ninja.HP)
#__init__
#este nuevo objeto posee los mismo atributos que el anterior
ninja_enemigo=NinjaPrincipal
#para modificar los atributos de un objeto en especifico
ninja_enemigo.HP=25
ninja_enemigo.resistencia=10"""

#self hace referencia acualquier nombre de objeto que creemos 
#se pone un self por metodo