try:
    nota = int(input("Ingresa tu nota (0 a 100): "))

    if nota < 0 or nota > 100:
        print("Nota inválida. Debe estar entre 0 y 100.")
    elif nota >= 90:
        print("Excelente")
    elif nota >= 70:
        print("Aprobado")
    else:
        print("Reprobado")

except ValueError:
    print("Debes ingresar un número entero válido.")

