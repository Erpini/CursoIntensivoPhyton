
#Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el
# parámetro que recibe la función.

#by Er Pini

n = int (input('Escribe tu numero'))

for i in range(2, n + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)