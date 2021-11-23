from skimage import filters
from skimage import exposure
from skimage.filters.rank import median
from skimage.morphology import disk
from skimage import restoration
from scipy.signal import convolve2d
from skimage import feature
import numpy as np
from skimage.color import rgb2gray

class FiltrosBordes:
    def __init__(self):
        print ("¡Filtros para detectar bordes creados!")

    def filtro_sobel(self, imagen):
        img = rgb2gray(imagen)
        return filters.sobel(img)

    def filtro_roberts(self, imagen):
        img = rgb2gray(imagen)
        return filters.roberts(img)

    def filtro_prewitt(self, imagen):
        img = rgb2gray(imagen)
        return filters.prewitt(img)