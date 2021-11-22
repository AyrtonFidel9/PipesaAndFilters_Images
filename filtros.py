from skimage import filters
from skimage import exposure
from skimage.filters.rank import median
from skimage.morphology import disk
from skimage import restoration
from scipy.signal import convolve2d
from skimage import feature
import numpy as np

class Filtros:
    def __init__(self):
        print ("¡Filtros creados!")

    def filtro_sobel(self, imagen):
        return filters.sobel(imagen)

    def filtro_roberts(self, imagen):
        return filters.roberts(imagen)

    def filtro_prewitt(self, imagen):
        return filter.prewitt(imagen)

    def filtro_estiramiento_contraste(self, imagen):
        p2, p98 = np.percentile(imagen, (2,98))
        return exposure.rescale_intensity(imagen, in_range=(p2,p98))

    def filtro_ecualizacion(self, imagen):
        return exposure.equalize_hist(imagen)

    def filtro_ecua_adaptativa(self, imagen):
        return exposure.equalize_adapthist(imagen, clip_limit=0.03)
    
    def filtro_eliminacion_ruido(self, imagen):
        return median(imagen)

    def filtro_restauracion(self, imagen):
        psf = np.ones((5,5)) / 25
        img = convolve2d(imagen, psf, 'same')
        img += 0.1 * img.std() * np.random.standard_normal((img.shape))
        return restoration.wiener(img, psf, 100)

    def filtro_suavizar_resalatar_contrastes(self, imagen):
        return feature.canny(imagen)