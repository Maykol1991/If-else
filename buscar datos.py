# Ubicar Dato
arreglo = [[12,13,14],[42,43,44],[72,73,74]]
index = int(input('ingrese el numero a buscar: '))
print("------------------------")
print("El arreglo es: " + str(arreglo))
print("------------------------")
for i in range(len(arreglo)):
    try:
        posicion = arreglo[i].index(index)
        print("el valor se encuentro en la lista " + str(i) + " la pocicion es: "+str(posicion))
    except ValueError:
        print("el valor no se encuentra en la lista " + str(i))
print("------------------------")