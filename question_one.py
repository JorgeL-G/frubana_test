#!/bin/python
from bisect import insort, bisect_left


def round_median(m):
    'Redondea a un decimal el parametro envio, si es .0 es llevado a su representacion entera'
    m = round(m, 1)
    if float(m).is_integer():
        return int(m)
    else:
        return m


def median(a, x):
    'Funcion que va imprimiendo la media de una lista ordenada que es modificada por las listas a y x'
    min_list = list()
    max_list = list()
    for operation, num in zip(a, x):
        flag = False
        # Se realizara la accion de agregar un elemento
        if operation == 'a':
            if len(min_list) == 0:
                insort(min_list, num)
            else:
                if num >= min_list[-1]:
                    insort(max_list, num)
                else:
                    insort(min_list, num)

        # Se realizara la accion de eliminar un elemento
        elif operation == 'r':
            min_index = bisect_left(min_list, num)
            max_index = bisect_left(max_list, num)
            if min_index != len(min_list) and min_list[min_index] == num:
                del(min_list[min_index])
            elif max_index != len(max_list) and max_list[max_index] == num:
                del(max_list[max_index])
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