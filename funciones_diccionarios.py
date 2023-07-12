import random
from funciones_archivos import *

def agregar_producto(lista_diccionarios:list):
    """
    Function: Agregar un producto a la lista anterior, se valida id y caracteristica.

    Args:
        lista_diccionarios (list): Lista anterior

    Returns:
        lista_diccionarios: Nueva lista con el producto agregado o no, dependiendo de si el id se repite.
    """
    nuevo_diccionario = {}

    for diccionario in lista_diccionarios:
        ultimo_id = int(diccionario["id"])                          # ID
    id_nuevo_producto = ultimo_id+1

    nombre = input("Ingrese nombre del producto:")                     # NOMBRE

    print()
    print("-----Marcas disponibles----")
    for marca in marcas_disponibles:
        print("-", marca)
    while True:                                                        # MARCA
        marca = input("Ingrese la marca: ")
        if marca in marcas_disponibles:
            break
        else:
            print("Marca inválida. Intente nuevamente.")

    precio = input("Ingrese precio del producto:")                    # PRECIO

    caracteristica = "Característica predefinida"
    while caracteristica == "Caracteristica predefinida" or len(caracteristica) > 3:
        caracteristica = input("Ingrese las características (separadas por comas): ").split(",")
        
        if caracteristica == "Característica predefinida" or len(caracteristica) > 3:
            print("Debe ingresar entre 1 y 3 características.")       # CARACTERISTICA
        else:
            break

    stock = input("Ingrese cantidad de stock del producto:")  
    
    for diccionario in lista_diccionarios:
        valores_diccionario = list(diccionario.values())
        if id_nuevo_producto in valores_diccionario :
            print("Al menos uno de los valores ya existe en los diccionarios anteriores.")
            return lista_diccionarios


    nuevo_diccionario['id'] = id_nuevo_producto
    nuevo_diccionario['nombre'] = nombre
    nuevo_diccionario['marca'] = marca
    nuevo_diccionario['precio'] = precio
    nuevo_diccionario['caracteristica'] = caracteristica
    nuevo_diccionario['stock'] = stock
    

    lista_diccionarios.append(nuevo_diccionario)
    return lista_diccionarios

def buscar_por_caracteristica(lista_diccionarios,caracteristica_ingresada)->list:
    """
    Function: Busca por la caracteristica ingresada y muestra los diccionarios que coincidan

    Args:
        lista_diccionarios (list): Lista que recibe
        caracteristica_ingresada (str): Caracteristica que buscara coincidencias
    
    Returns:
        lista_diccionarios (dict): Lista que tiene los diccionarios que coinciden con la caracteristica

    """
    lista_caracteristica = []
    for diccionario in lista_diccionarios:
        if 'caracteristica' in diccionario and str(caracteristica_ingresada) in diccionario['caracteristica']:
            lista_caracteristica.append(diccionario)

    if lista_caracteristica == []:
        print("-NO EXISTEN PRODUCTOS CON ESA CARACTERISTICA-")
    else:     
        print("═══════════════════════════════════════════════════════════════════════ FILTRADO CARACTERISTICA ═══════════════════════════════════════════════════════════════════════")
        for diccionario in lista_caracteristica:
            print(diccionario)                                             # Muestro con un espacio entre cada diccionario
            print() 
    os.system("pause")
    os.system("cls")
    return lista_caracteristica

def ordenar_lista(lista_diccionarios: list, clave_principal: str, clave_auxiliar: str) -> list:
    """
    Function: Ordena la lista según el abecedario de forma ascendente según la clave especificada.

    Args:
        lista_diccionarios (list): Lista a ordenar.
        clave_principal (str): Clave principal para el ordenamiento.
        clave_auxiliar (str): Clave auxiliar para el ordenamiento secundario.

    Returns:
        list: Lista ordenada de forma ascendente.
    """

    lista_ordenada = lista_diccionarios[:]  # Crear una copia de la lista original

    tam = len(lista_ordenada)

    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista_ordenada[i][clave_principal] > lista_ordenada[j][clave_principal] or (
                    lista_ordenada[i][clave_principal] == lista_ordenada[j][clave_principal] and
                    float(lista_ordenada[i][clave_auxiliar]) > float(lista_ordenada[j][clave_auxiliar])):
                lista_ordenada[i], lista_ordenada[j] = lista_ordenada[j], lista_ordenada[i]

    print("═══════════════════════════════════════════════════════════════════════ DATOS ORDENADOS ═══════════════════════════════════════════════════════════════════════")
    for diccionario in lista_ordenada:
        print(diccionario)  # Muestro con un espacio entre cada diccionario
        print()

    os.system("pause")
    os.system("cls")

    return lista_ordenada

def aplicar_aumento_dic(diccionario):
    precio = float(diccionario["precio"]) 
    aumento = precio * 0.084
    precio_con_aumento = precio + aumento
    diccionario["precio"] = precio_con_aumento
    return diccionario

def mostrar_diccionarios(lista):
    for diccionario in lista:
        print (diccionario)
        print()

def contar_en_lista(lista_dic:list,key:str)->dict:
    """
    Function: Recibe una lista de diccionarios y una clave, agrega esos valores de la clave a una lista y luego recorre la lista agregandolos a un diccionario, si ya estaban, cuenta.
    Por ultimo muestra de forma prolija los valores con su contador de veces que estan.

    Args:
        lista_dic (list): Lista que recibe
        key (str): Clave que usara sus valores para contarlos
    
    Returns:
        diccionario (dict): Diccionario con los valores sin repetir y contados.

    """
    lista_aux=[]
    diccionario = {}

    for clave in lista_dic:                    # Agrego a una lista las claves
        lista_aux.append(clave[key])
    for elemento in lista_aux:
        if elemento in diccionario:
            diccionario[elemento] += 1         # Si el elemento ya existe en el diccionario, los voy contando.
        else:
            diccionario[elemento] = 1
    print()
    print("MARCAS DISPONIBLES Y CANTIDAD DE INSUMOS:")
    for elemento in diccionario:               # Muestro de forma prolija
        cantidad = diccionario[elemento]
        print(f"{elemento}: {cantidad}")

    os.system("pause")
    os.system("cls")
    return diccionario

def mostrar_dos_claves(lista_dic:list,key:str,key_2:str)->list:
    """
    Function: Recibe una lista de diccionarios y tres claves,termina reduciendo la lista original agregando las claves con diccionarios a una nueva lista.

    Args:
        lista_dic (list): Lista de diccionarios que recibe
        key (_type_): Clave nro 1
        key_2 (_type_): Clave nro 2
        key_3 (_type_): Clave nro 3

    Returns:
        lista_reducida (list): Lista de diccionarios reducida a tres diccionarios
    """
    diccionario={}
    lista_reducida=[]
    for clave in lista_dic:
        diccionario = {
                "marca": clave[key],
                "stock": clave[key_2],                                           # Creo los diccionarios
            } 
        lista_reducida.append(diccionario)
    print("═══════════════════════════════════════════════════════════════════════ MARCAS DISPONIBLES CON SU STOCK ═══════════════════════════════════════════════════════════════════════")
    for diccionario in lista_reducida:
        print(diccionario)                                             # Muestro con un espacio entre cada diccionario
        print() 

    os.system("pause")
    os.system("cls")
    return lista_reducida

def mostrar_tres_claves(lista_dic:list,key:str,key_2:str,key_3:str)->list:
    """
    Function: Recibe una lista de diccionarios y tres claves,termina reduciendo la lista original agregando las claves con diccionarios a una nueva lista.

    Args:
        lista_dic (list): Lista de diccionarios que recibe
        key (_type_): Clave nro 1
        key_2 (_type_): Clave nro 2

    Returns:
        lista_reducida (list): Lista de diccionarios reducida a tres diccionarios
    """
    marcas = {}

    for clave in lista_dic:
        marca = clave[key]
        nombre = clave[key_2]
        precio = clave[key_3]

        if marca in marcas:
            marcas[marca].append({"nombre": nombre, "precio": precio})
        else:
            marcas[marca] = [{"nombre": nombre, "precio": precio}]

    print("═══════════════════════════════════════════════════════════ MARCAS Y SUS INSUMOS ═══════════════════════════════════════════════════════════ ")
    
    for marca, productos in marcas.items():
        print(f"Marca: {marca}")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")
        print()

    os.system("pause")
    os.system("cls")
    return lista_dic

def agregar_campo_a_diccionarios(lista_diccionarios, nuevo_campo):
    return list(map(lambda diccionario: agregar_campo(diccionario, nuevo_campo), lista_diccionarios))

def agregar_campo(lista_diccionario, nuevo_campo):
    lista_diccionario[nuevo_campo] = random.randint(0, 10)
    return lista_diccionario
