# ✅ ¿Qué es un bucle?

# Un bucle (loop) repite instrucciones mientras se cumple una condición.
# Sirve, por ejemplo, para:
#     Mostrar una lista de elementos
#     Pedir datos varias veces
#     Repetir cálculos
#     Contar


# 🔁 Bucle for
# 📌 Se usa cuando sabes cuántas veces quieres repetir algo.
for i in range(5):
    print("Hola", i)

# 🔄 Bucle while
# 📌 Se usa cuando quieres repetir algo hasta que se cumpla una condición.
contador = 1
while contador <= 5:
    print("Contando:", contador)
    contador += 1   # contador = contador + 1

for i in range(1, 11): # No incluye el ultimo numero
    print(i)


print("contador")
contador = 10
while(contador > 0):
    print(contador)
    contador -= 1