import os , time , csv 
from funcionesbus import *
ventasbus = []


while True:
    print("menu de opciones")
    print("1. Mostrar asientos disponibles")
    print("2. Comprar asientos")
    print("3. Mostrar ventas realizadas")
    print("4. Generar archivo csv")
    print("5. Salir")
    opc = int(input("Ingrese una opcion: "))
    os.system('cls')

    if opc ==1:
        mostrar_asientos()
    elif opc ==2:
        comprar_asiento()
    elif opc ==3:
        mostrar_venta_realizada()
    elif opc ==4:
        Generar_archivocsv()
    else:
        print("Gracias por su compra, hasta pronto!")
        time.sleep(3)

    