# link https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator


from copy import copy
import random

class Hat:
    
    def __init__(self,**bolas) -> None:
        self.dictbolas = bolas
        self.contents = []
        # paso el diccionario del kwargs a una lista simple con elementos repetidos
        for key,value in self.dictbolas.items():
            for _ in range(int(value)):
                self.contents.append(key)
                
    def draw(self,draw):
        # IMPORTANTE: creo una copia de la lista inicial de la clase, ya que sino esta se vacia porque no se renueva el objeto
        bolsa = copy(self.contents)
        # me fijo que no me pida sacar + elementos de los que tengo en la lista
        if draw > len(bolsa):
            return self.contents
        self.afuera = []
        # consigo un elemento aleatorio de la copia de la lista y lo saco
        for _ in range(draw):
            aleatorioElemento = random.choice(bolsa)
            bolsa.remove(aleatorioElemento)
            self.afuera.append(aleatorioElemento)
        return self.afuera
        # cuando vuelva a iniciar el loop habra una nueva copia de la lista orginal creada con todos los elemento y se aleatorizará de nuevo
    


def experiment(hat,num_experiments,num_balls_drawn,expected_balls=None):
    m = 0

# convierto los numeros sacados en un diccionario para que sea mas facil de comparar
    for _ in range(num_experiments):
        contador = 0
        pool = hat.draw(num_balls_drawn)
        grouper = {}
        for item in pool:
            grouper[item] = 0
        for item in pool:
            if grouper[item] is not True:
                grouper[item] +=1
        
        # comparo ambos diccionarios 
        try:
            for key,value in expected_balls.items():
                if expected_balls[key] == grouper[key]:
                    contador += 1
                if contador == len(expected_balls):
                    m += 1
        except:
            pass
            
        
        
    resultado = m/num_experiments
    return float(resultado)


        
            
            
            



# hat = Hat(black=6, red=4, green=3)
# probability = experiment(hat=hat,
#                   expected_balls={"red":2,"green":1},
#                   num_balls_drawn=5,
#                   num_experiments=1000)



        






    
        
        
    
    
    

        
    
    
    
    

    
