from warnings import filters
import os
from skimage import io
from skimage.color import rgb2gray
from filtros import Filtros
from Tuberias import Tuberia

def menu():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print ("Selecciona una opción")
    print ("\t1 - Mejoramiento de contraste")
    print ("\t2 - Eliminacion de ruido")
    print ("\t3 - Restauracion")
    print ("\t4 - Suavizar")
    print ("\t5 - Detección de bordes")
    print ("\t9 - salir")

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
    filtro = Filtros()

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
            tuberia.add([filtro.filtro_estiramiento_contraste,
                         filtro.filtro_ecualizacion,
                         filtro.filtro_ecua_adaptativa])
            tuberia.ejecutar(imagen, 0)
        
        elif opcionMenu=="2":
            print ("")
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")
            ##Eliminación de ruido
            imagen = io.imread("charlie.jpg")
            img_gray = rgb2gray(imagen)
            tuberia.add([filtro.filtro_eliminacion_ruido])
            tuberia.ejecutar(imagen, 0)
            
        elif opcionMenu=="3":
            print ("")
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")
            ##Restauracion
            imagen = io.imread("imagen_ruido.jpg")
            img = rgb2gray(imagen)
            tuberia.add([filtro.filtro_restauracion])
            tuberia.ejecutar(img,0)
            
        elif opcionMenu=="4": 
            ##suavizar 
            imagen = io.imread("mario.jpg")
            img = rgb2gray(imagen)
            tuberia.add([filtro.filtro_suavizar_resalatar_contrastes])
            tuberia.ejecutar(img,0)
        
        elif opcionMenu=="5":
            ##detección de bordes
            menu_bordes()
            imagen_g = rgb2gray(imagen)
            opcionMenuBordes = input("inserta un numero valor >> ")
            if opcionMenuBordes == "1":
                tuberia.add([filtro.filtro_sobel])
                tuberia.ejecutar(imagen_g, 0)
            elif opcionMenuBordes == "2":
                tuberia.add([filtro.filtro_roberts])
                tuberia.ejecutar(imagen_g, 0)
            elif opcionMenuBordes == "3":
                tuberia.add([filtro.filtro_prewitt])
                tuberia.ejecutar(imagen_g, 0)
            elif opcionMenuBordes == "9":
                menu()
        elif opcionMenu=="9":
            break
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    pass 

