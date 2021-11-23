from skimage import filters
from skimage import exposure
from skimage.filters.rank import median
from skimage.morphology import disk
from skimage import restoration
from scipy.signal import convolve2d
from skimage import feature
import numpy as np

class FiltroRestauracion:
    def __init__(self):
        print ("¡Filtros creados!")

    def filtro_restauracion(self, imagen):
        psf = np.ones((5,5)) / 25
        img = convolve2d(imagen, psf, 'same')
        img += 0.1 * img.std() * np.random.standard_normal((img.shape))
        return restoration.wiener(img, psf, 100)