import os
import json

def menu():
    os.system("cls")
    try:
        print("════════════════════════════════════════   MENU   ════════════════════════════════════════")
        print("")
        print("1-  Cargar datos del archivo (obligatorio)")
        print("2-  Mostrar marcas y insumos de cada una")
        print("3-  Mostrar para cada marca el nombre y el precio de los insumos")
        print("4-  Buscar por caracteristica")
        print("5-  Mostrar productos ordenados por marcas de forma ascendente")
        print("6-  Realizar Compras")
        print("7-  Guardar en JSON por producto que diga Alimento")
        print("8-  Leer el JSON")
        print("9-  Actualizar Precios en 8.4%")
        print("10- Salir")
        print("════════════════════════════════════════ EXTRA ════════════════════════════════════════")
        print("11- Agregar producto")
        print("12- Generar archivo .csv o .json con los productos agregados")

        
        opcion=int(input("Ingrese una opcion:"))
        
        return opcion

    except ValueError:
        print("----------------OPCION INVALIDA--------------------")
        os.system("pause")
        os.system("cls")

def cargar_archivo(nombre_archivo)->list:
    """
    Function: 
        Ingresa direccion del archivo a cargar, por ejemplo: 'carpeta//ejemplo.csv'.

    Args:
        nombre_archivo (str): Archivo a cargar

    Returns:
        Se carga el archivo en formato de lista de diccionarios y los muestra.
    """
    os.system("cls")
    separador = ","


    with open(nombre_archivo, encoding="utf-8") as archivo:
        lista_diccionario = []
        for linea in archivo:
            linea = linea.strip("\n").replace("$", "")                                  # Saco el salto de linea y elimino $
            columnas = linea.split(separador)                                           # Separo con , los datos

            id, nombre, marca, precio, caracteristica = columnas                        # Asigno las columnas

            diccionarios = {
                "id": id,
                "nombre": nombre,
                "marca": marca,                                                         # Creo los diccionarios
                "precio": precio,
                "caracteristica": caracteristica
            }                                           

            lista_diccionario.append(diccionarios)                                      # Los agrego a la lista_diccionario

        # print("═══════════════════════════════════════════════════════════════════════ DATOS DEL ARCHIVO ═══════════════════════════════════════════════════════════════════════")
        # for diccionario in lista_diccionario:
        #     print(diccionario)                                                          # Muestro con un espacio entre cada diccionario
        #     print() 

        # os.system("pause")
        # os.system("cls")

        return lista_diccionario

def comprar(lista_diccionarios: list) -> list:
    lista_caracteristica = []
    while lista_caracteristica == []:
        marca_elegida = input("Ingrese marca: ").lower()

        for diccionario in lista_diccionarios:
            diccionario["marca"] = diccionario["marca"].lower()
            if marca_elegida in diccionario.values():
                lista_caracteristica.append(diccionario)
        if lista_caracteristica == []:
            print("La marca \"", marca_elegida, "\" no existe, reintente con otra.")
            print()
        else:
            print("PRODUCTOS DISPONIBLES:")
            print()
            for diccionario_marca in lista_caracteristica:
                print(diccionario_marca)
                print()
            break

    carrito = []

    while True:
        producto_id = input("Ingrese el ID del producto que desea comprar (0 para finalizar): ")

        if producto_id == "":
            print("Debe ingresar un ID de producto válido.")
            continue

        if producto_id == "0":
            if carrito == []:
                print("El carrito está vacío. Por favor, seleccione al menos un producto.")
                continue
            else:
                break

        cantidad = int(input("Ingrese la cantidad: "))

        producto_seleccionado = None
        producto_encontrado = False
        for diccionario in lista_caracteristica:
            if str(producto_id) == str(diccionario['id']):
                producto_encontrado = True
                if diccionario['stock'] == "0":
                    print("El producto seleccionado no tiene stock. Por favor, elija otro producto.")
                    break
                elif cantidad > int(diccionario['stock']):
                    print("La cantidad seleccionada supera el stock disponible. Por favor, ingrese una cantidad menor.")
                    break
                else:
                    producto_seleccionado = diccionario
                    producto_seleccionado['cantidad'] = cantidad
                    carrito.append(producto_seleccionado)
                    int(diccionario["stock"]) - cantidad
                    print("Producto agregado al carrito.")
                    break

        if not producto_encontrado:
            print("No se encontró ningún producto con el ID ingresado. Por favor, ingrese un ID válido.")

        print()
        respuesta = input("¿Desea elegir otro producto? (s/n): ")
        if respuesta.lower() != "s":
            break

    if carrito:
        print("════════════ CARRITO:")
        for producto in carrito:
            print(producto)

    return carrito

def generar_archivo_txt(carrito, nombre_archivo:str):
    try:
        with open(nombre_archivo, 'w') as archivo:
            total = 0.0 
            
            for producto in carrito:
                archivo.write(str(producto) + '\n')
                precio = float(producto['precio'])
                cantidad = int(producto['cantidad'])
                total += precio * cantidad              # Calcular el total
                
            archivo.write(f"Total: ${total}\n")         # Escribir el total en el archivo
            
        print(f"El archivo {nombre_archivo} se ha generado correctamente.")
        os.system("pause")
        os.system("cls")
    except IOError:
        print("Se produjo un error al generar el archivo.")
        os.system("pause")
        os.system("cls")

def guardar_JSON(lista_de_productos,path):
    lista_filtrada=[]
    for producto in lista_de_productos:
        if ("Alimento" in producto['nombre']):
            lista_filtrada.append(producto)
    with open (path,"w") as file:
        json.dump(lista_filtrada,file,indent=4)

def leer_JSON(path):
    lista_leida=[]
    with open(path) as file:
        lista_leida=json.load(file)
    print("-ARCHIVO LEIDO-")
    for diccionario in lista_leida:
        print(diccionario)
        print()
    return lista_leida

def guardar_csv(lista_aumentada,direccion_archivo_nuevo):
    with open(direccion_archivo_nuevo,"w",encoding="utf-8") as file:
        renglon = 0
        for i in lista_aumentada:
            linea= f'{i["id"]},{i["nombre"]},{i["marca"]},${i["precio"]},{i["caracteristica"]}'
            file.writelines("\n")
            file.writelines(linea)
            renglon+=1
        print("Datos guardados en el archivo CSV correctamente.")
    os.system("pause")
    os.system("cls")

def leer_marcas():
    marcas = []
    with open("marcas.txt", "r") as archivo:
        for linea in archivo:
            marca = linea.strip()
            marcas.append(marca)
    
    return marcas

marcas_disponibles = leer_marcas()

def guardar_json_csv(lista:list,direccion_archivo_nuevo,guardar_json_o_csv:str):
    """
    Function: Recibe una lista que la transformara en json o csv segun el usuario ingrese, guardara en el segundo parametro el archivo.

    Args:
        lista (list): Lista a transformar
        direccion_archivo_nuevo (path): Donde se guardara, Indicar .csv o .json al final
        guardar_json (True): JSON por defecto

    Returns:
        Archivo nuevo.
    """
    if guardar_json_o_csv == "json":
        lista_json=[]
        for producto in lista:
            lista_json.append(producto)
        with open (direccion_archivo_nuevo,"w") as file:
            json.dump(lista_json,file,indent=4)
    else:
        with open(direccion_archivo_nuevo,"w",encoding="utf-8") as file:
            renglon = 0
            for i in lista:
                linea= f'{i["id"]},{i["nombre"]},{i["marca"]},${i["precio"]},{i["caracteristica"]}'
                file.writelines("\n")
                file.writelines(linea)
                renglon+=1

    print("Datos guardados en el archivo correctamente.")
    os.system("pause")
    os.system("cls")

def seguir_salir():
    """
    Function: 
        Nos pregunta si deseamos continuar o finalizar un programa
    Returns:
        Nos retorna una respuesta, si es "S" continua, si no, finaliza el programa
    """
    continuar_salir=input("Desea continuar? s/n: ")
    while continuar_salir != "s" and continuar_salir != "n":
        continuar_salir=input("ERROR, desea continuar? s/n: ")
    if continuar_salir =="n":
        quit("----------------------------FIN DEL PROGRAMA-------------------------------")
