# # # 🧪 Lista de ejercicios para practicar ciclos
# # # 1. Contador ascendente
# # # Muestra los números del 1 al 20, uno por línea.
# # print("Del 1 al 20")
# # for i in range(1,21): 
# #     print(i)

# # # 2. Suma de pares
# # # Suma todos los números pares entre 1 y 100 y muestra el resultado.
# # print("Numeros pares")
# # contador = 2
# # while contador <= 100:
# #     print(contador)
# #     contador += 2

# # # 3. Tabla de multiplicar
# # # Pide un número entre 1 y 10, y muestra su tabla de multiplicar hasta el 10.
# # print("Tabla de multiplicar")
# # num = int(input("Ingresa un numero entre el 1 al 10: "))
# # if num > 0 and num < 11:
# #     for i in range(1,11):
# #         res = num * i 
# #         print(res)
# # else:
# #     print("Debes ingresar un numero entre 1 y 10")
    
# # # 4. Letra por letra
# # # Pide al usuario un nombre y muestra cada letra por separado.


# # # 5. Cuenta regresiva
# # # Muestra los números del 10 al 1.
# # print("Del 10 al 1")
# # for i in range (10, 0, -1):
# #     print(i)

# # # 6. Contraseña
# # # Pide una contraseña al usuario. Si no escribe "python123", vuelve a pedirla. Termina solo cuando escriba la correcta.
# # password = "python123"
# # contador = 1
# # passwordInput = input("Ingrese contraseña: ")
# # while(password != passwordInput):
# #     print("Contraseña incorrecta")
# #     passwordInput = input("Ingrese contraseña: ")

# # print("Contraseña correcta")    

# # # 7. Menú interactivo
# # # Muestra este menú de opciones hasta que el usuario elija "3":
# # # 1. Saludar
# # # 2. Decir tu nombre
# # # 3. Salir

# opcion = 0

# while opcion != 3:
#     opcion = int(input("Ingresa un número del 1 al 3:\n1. Saludar\n2. Decir tu nombre\n3. Salir\n"))

#     if opcion == 1:
#         print("Hola!!!")
#     elif opcion == 2:
#         print("Soy Lian")
#     elif opcion == 3:
#         print("Saliste del programa.")
#     else:
#         print("Opción inválida, intenta de nuevo.")

# 🧩 Ejercicio 1: Registro de notas con validación y promedio
# Requisitos:
#     Pide al usuario ingresar notas una por una.
#     Solo acepta números del 1.0 al 7.0. Si no, muestra error y vuelve a pedir.
#     El usuario puede escribir "fin" para terminar.
#     Al final, muestra:
#     El total de notas ingresadas.
#     El promedio.
#     La nota más alta y la más baja.

