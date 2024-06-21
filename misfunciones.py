import csv 
import os
import msvcrt

productos = []



def limpiar():
        print("<<Press any key>>")
        msvcrt.getch()
        os.system("cls")


def printR(texto):
    print(f"\033[31m{texto}\033[0m")

def printV(texto):
    print(f"\033[32m{texto}\033[0m")

def printA(texto):
    print(f"\033[33m{texto}\033[0m")


def menu():
    printA("🎮 Sistema Gestión de TechStore 🎧")
    printA("════════════════════════════════")
    print("1.	Agregar un nuevo producto al inventario.")
    print("2.	Mostrar el inventario")
    print("3.	Vender un producto")
    print("4.	Guardar el inventario en un archivo CSV")
    print("5.	Cargar el inventario desde un archivo CSV.")
    print("0.	Salir del programa")
    printA("════════════════════════════════")


def agregar_producto(inventario,nombre,precio,cantidad):
     productos = [nombre,precio,cantidad]
     inventario = []
     inventario.append(productos)
     return inventario

def mostrar_inventario(inventario):
     for productos in inventario:
        print(f"NOMBRE : {productos[0]}, PRECIO : {productos[1]}, CANTIDAD: {productos[2]}")

def vender_producto(inventario,nombre,cantidad):
     for productos in inventario:
          if productos[0] == nombre:
               if productos[2] >= cantidad:
                    productos[2] -= cantidad
                    total = productos[1] * cantidad 
                    return total
               else:
                    print("No hay suficiente cantidad en el stock.")


def guardar_inventario(nombre,inventario,archivo,precio,cantidad):
     with open(archivo,'w',newline='') as file:
          writer = csv.writer(file)
          writer.writerow([nombre,precio,cantidad])
          for productos in inventario:
               writer.writerow(productos)

def cargar_inventario(archivo):
    inventario = []
    with open(archivo, 'r') as file:
         reader = csv.reader(file)
         next(reader)
         for row in reader:
              inventario.append(row)
              return inventario
    
     




     
