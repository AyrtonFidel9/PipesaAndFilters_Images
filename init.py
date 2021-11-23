from warnings import filters
import os
from skimage import io
from skimage.color import rgb2gray
from Filtro_Suavizar_Cont import FiltroSuavizar
from Filtro_Deteccion_Bordes import FiltrosBordes
from Filtro_Mejor_Contraste import FiltroMejContraste
from Filtro_Eliminacion_Ruido import FiltroRuido
from FiltroRestauracion import FiltroRestauracion
from Tuberias import Tuberia

def menu():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print ("Selecciona una opción")
    print ("\t1 - Mejoramiento de contraste")
    print ("\t2 - Eliminacion de ruido")
    print ("\t3 - Restauracion")
    print ("\t4 - Suavizar y resaltar contornos")
    print ("\t5 - Detección de bordes")
    print ("\t9 - salir")
55

def menu_bordes():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print ("Selecciona una opción")
    print ("\t1 - Filtro sobel")
    print ("\t2 - Filtro roberts")
    print ("\t3 - Filtro prewitt")
    print ("\t9 - salir")

if __name__=='__main__': 
    ##se llama a los filtros y tuberias
    tuberia = Tuberia()
    suavizar = FiltroSuavizar()
    bordes = FiltrosBordes()
    contraste = FiltroMejContraste()
    ruido = FiltroRuido()
    restauracion = FiltroRestauracion()
    ##lectura de la imagen
    imagen = io.imread("imagen.jpg")
    
    while True:
        # Mostramos el menu
        menu()
        # solicituamos una opción al usuario
        opcionMenu = input("inserta un numero valor >> ")
    
        if opcionMenu=="1":
            print ("")
            input("Has pulsado la opción 1...\npulsa una tecla para continuar")
            ##Mejoramiento de contraste
            tuberia.add([contraste.filtro_estiramiento_contraste,
                         contraste.filtro_ecualizacion,
                         contraste.filtro_ecua_adaptativa])
            tuberia.ejecutar(imagen, 0)
        
        elif opcionMenu=="2":
            print ("")
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")
            ##Eliminación de ruido
            imagen = io.imread("charlie.jpg")
            img_gray = rgb2gray(imagen)
            tuberia.add([ruido.filtro_eliminacion_ruido])
            tuberia.ejecutar(imagen, 0)
            
        elif opcionMenu=="3":
            print ("")
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")
            ##Restauracion5
            imagen = io.imread("imagen_ruido.jpg")
            img = rgb2gray(imagen)
            tuberia.add([restauracion.filtro_restauracion])
            tuberia.ejecutar(img,0)
            
        elif opcionMenu=="4": 
            ##suavizar 
            imagen = io.imread("mario.jpg")
            img = rgb2gray(imagen)
            tuberia.add([suavizar.filtro_suavizar_resalatar_contrastes])
            tuberia.ejecutar(img,0)
        
        elif opcionMenu=="5":
            ##detección de bordes
            menu_bordes()
            imagen = io.imread("imagen.jpg")
            imagen_g = rgb2gray(imagen)
            opcionMenuBordes = input("inserta un numero valor >> ")
            if opcionMenuBordes == "1":
                tuberia.add([bordes.filtro_sobel])
                tuberia.ejecutar(imagen_g, 0)
            elif opcionMenuBordes == "2":
                tuberia.add([bordes.filtro_roberts])
                tuberia.ejecutar(imagen_g, 0)
            elif opcionMenuBordes == "3":
                tuberia.add([bordes.filtro_prewitt])
                tuberia.ejecutar(imagen_g, 0)
            elif opcionMenuBordes == "9":
                menu()
        elif opcionMenu=="9":
            break
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    pass 

