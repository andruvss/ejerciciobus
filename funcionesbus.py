import os , csv , time 

tarifabus = 5000
descuentomenor = 0.2
descuentomayor = 0.15
ventasbus = []
bus = [["O" for x in range(4)]for y in range(7)]
bus [1][1] = "x"

def mostrar_asientos():
    bus = [["O" for x in range(4)]for y in range(7)]
    bus [1][1] = "x" 
   
    for x in bus:
        print(x)



def comprar_asiento():
    while True:
        nombre = input("Ingrese su nombre")
        if nombre > 3 and nombre.isalpha():
            break
        else:
            print("Escoja un nombre valido!")
    while True:
        try:
            edad = int(input("Ingrese su edad"))
            if edad > 0 and edad < 120:
                break
            else:
                print("ERROR elija una edad entre 0 y 120")
        except:
            print("Escoja un numero entero")
    while True:
        try:
            telefono = int(input("Ingrese su numero de telefono:"))
            if len(telefono)==9:
                break
            else:
                print("ingrese un numero de telefono valido!")
        except:
            print("Debe contener caracteres numericos!")
    while True:
        filaelejir = input("Ingrese una fila deseada")
        columnaelejir = input("Ingrese una columna")
        if bus[filaelejir-1][columnaelejir-1]=="O":
            bus[filaelejir-1][columnaelejir-1]= 'x'
            print("Asiento escojido correctamente")
            break
        else:
            print("asiento ocupado")

    clientebus = {"Nombre": nombre , "EDAD": edad, "TELEFONO": telefono, "FILA": filaelejir, "COLUMNA": columnaelejir}
    ventasbus.append(clientebus)

    print("SU EDAD ES DE: ", edad)
    if edad < 18:
        preciomenor18 = tarifabus*0.2
        print("Su descuento fue de un 0.2% al tener menos de 18 anios ", preciomenor18)
    else:
        print("EXISTE DESCUENTO PARA MENORES DE 18 Y  MAYORES DE 65")

    if edad > 65:
        preciomayor = tarifabus*0.15
        print("Su tarifa se le aplico un descuento del 0.15% ", preciomayor)


def mostrar_venta_realizada():
    if not ventasbus:
        print("NO EXISTE COMPRA DE ASIENTO!, ")
    else:
        print("\tMOSTRAR VENTA REALIZADA")
        for x in ventasbus:
            print(f"Nombre : {x['nombre']}\nEDAD: {x['edad']}\nTELEFONO: {x['telefono']}\nFILA: {x['fila']}\nCOLUMNA: {x['columna']}\n")


def Generar_archivocsv():
    if len(ventasbus)== 0:
        print("Lista vacia!")
    else:
        with open("archivodevuses.csv","w",newline="")as archivo:\
        escritor = csv.DictWriter(archivo, ["Nombre","Edad","Telefono","Fila","Columna"])
        escritor.writerows(ventasbus)
        print("Archivo creado con exito!")



       







