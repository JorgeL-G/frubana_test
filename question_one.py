#!/bin/python
from bisect import insort

# Funcion que recibe como parametro un numero entero o flotante.
# EL cual es redondeado a un decimal, si este resulta ser 0, es
# numero en llevado a su representacion en entero
def round_median(m):
    m = round(m, 1)
    if float(m).is_integer():
        return int(m)
    else:
        return m

# Funcion que recibe como parametro dos listas, la primera contiene las
# acciones a ejecutar y una segunda lista contiene numeros enteros.
#
# El procedimiento para el ir obteniendo la mediana de la lista, se hara
# por medio de dos listas.
def median(a, x):
    min_list = list()
    max_list = list()
    for operation, number in zip(a, x):
        flag = False
        # Se realizara la accion de agregar un elemento
        if operation == 'a':
            if len(min_list) == 0:
                insort(min_list, number)
            else:
                if number >= min_list[-1]:
                    insort(max_list, number)
                else:
                    insort(min_list, number)

        # Se realizara la accion de eliminar un elemento
        elif operation == 'r':
            if number in min_list:
                min_list.remove(number)
            elif number in max_list:
                max_list.remove(number)
            else:
                flag = True

        else:
            flag = True

        # Se equilibra las longitudes de las dos listas
        if len(max_list) > len(min_list):
            first_element = max_list[0]
            del max_list[0]
            min_list.append(first_element)

        if len(min_list) > (len(max_list) + 1):
            last_element = min_list[-1]
            del min_list[-1]
            max_list.insert(0,last_element)

        # Se procede al calculo de la mediana
        if flag or (len(min_list) == 0 and len(max_list) == 0):
            print('Wrong!')
        elif len(min_list) > len(max_list):
            new_median = round_median(min_list[-1])
            print(new_median)
        elif len(min_list) == len(max_list):
            new_median = (min_list[-1] + max_list[0]) / 2
            new_median = round_median(new_median)
            print(new_median)
        else:
            print('Wrong!')


N = int(input())
s = []
x = []
for i in range(0, N):
   tmp = input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))

median(s, x)
