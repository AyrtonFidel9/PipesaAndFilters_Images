from skimage import filters
from skimage import exposure
from skimage.filters.rank import median
from skimage.morphology import disk
from skimage import restoration
from scipy.signal import convolve2d
from skimage import feature
import numpy as np

class FiltroMejContraste:
    def __init__(self):
        print ("¡Filtros para el mejoramiento de contraste creados!")

    def filtro_estiramiento_contraste(self, imagen):
        p2, p98 = np.percentile(imagen, (2,98))
        return exposure.rescale_intensity(imagen, in_range=(p2,p98))

    def filtro_ecualizacion(self, imagen):
        return exposure.equalize_hist(imagen)

    def filtro_ecua_adaptativa(self, imagen):
        return exposure.equalize_adapthist(imagen, clip_limit=0.03)