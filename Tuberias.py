# Librerias necesarias
import matplotlib.pyplot as plt

class Tuberia:
    def __init__(self):
        print("¡Tuberia creada!")
        self.filters = list()
        pass
    def add (self, filtro):
        self.filters.extend(filtro)
        pass

    def ejecutar(self, imagen, lon):
        fil = self.filters
        if(lon < len(self.filters)):
            imagen_con_filtro = fil[lon](imagen)
            lon = lon + 1
            #plt.imshow(imagen_con_filtro)
            #plt.show()
            self.ejecutar(imagen_con_filtro,lon)
        else:
            print("Resultado")
            plt.imshow(imagen)
            plt.show()
            self.filters.clear() ## se limpian los filtros aplicados
            return

            


