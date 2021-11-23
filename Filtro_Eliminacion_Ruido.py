from skimage import filters
from skimage import exposure
from skimage.filters.rank import median
from skimage.morphology import disk
from skimage import restoration
from scipy.signal import convolve2d
from skimage import feature
import numpy as np

class FiltroRuido:
    def __init__(self):
        print ("¡Filtros para la eliminacion de ruido creados!")

    def filtro_eliminacion_ruido(self, imagen):
        return median(imagen)