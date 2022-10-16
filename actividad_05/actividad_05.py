from _particula import Particula
from lista_particulas import Lista_Particulas

particula_1 = Particula(0,0.2,0.2,0.4,0.4,0.1,1,2,3)
particula_2 = Particula(1,0.3,0.3,0.5,0.5,0.1,2,3,4)
particula_3 = Particula(2,0.4,0.4,0.6,0.6,0.1,4,5,6)
particula_4 = Particula(3,0.4,0.4,0.6,0.6,0.1,7,8,9)

lista = Lista_Particulas()

lista.insertar_inicio(particula_4)
lista.insertar_inicio(particula_3)
lista.insertar_final(particula_1)
lista.insertar_final(particula_2)

lista.mostrar()