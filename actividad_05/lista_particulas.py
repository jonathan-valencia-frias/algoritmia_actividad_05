from _particula import Particula

class Lista_Particulas:
    lt_particula=list()
    
    def insertar_inicio(self,p):
        self.lt_particula.insert(0,p)
    def insertar_final(self,p):
        self.lt_particula.append(p)
    def mostrar(self):
        for i in range(len(self.lt_particula)):
            print(str(self.lt_particula[i])+"\n")