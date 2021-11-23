from skimage import filters
from skimage import exposure
from skimage.filters.rank import median
from skimage.morphology import disk
from skimage import restoration
from scipy.signal import convolve2d
from skimage import feature
import numpy as np

class FiltroSuavizar:
    def __init__(self):
        print ("¡Filtros para suavizar y resaltar contornos creados!")

    def filtro_suavizar_resalatar_contrastes(self, imagen):
        return feature.canny(imagen)