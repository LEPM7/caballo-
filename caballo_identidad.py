import sys
#libreria para obtener el tiempo actual y cuando termino el metodo
import time
#libreria numpy para trabajar arreglos de manera rapida
import numpy as np
#libreria importada copy para copiar arreglos de manera mas eficiente
from copy import deepcopy

##############################################################################################
##############################################################################################
##########################   V A R I A B L E S   #############################################
##############################################################################################
##############################################################################################

# limites del tablero

max_x = 2
max_y = 2
min_x = 0
min_y = 0
caballos = ['Cb','Cn']
nodo_inicio = [['Cn', '0', 'Cn'], ['0', '0', '0'], ['Cb', '0', 'Cb']]
nodo_fin = [['Cb', '0', 'Cb'], ['0', '0', '0'], ['Cn', '0', 'Cn']]
nodos_sucesores = []

##############################################################################################
##############################################################################################
######################### M E T O D O S  C O M U N E S  ##### ################################
##############################################################################################
##############################################################################################

def imprimir_papas(nodo):
    x = len(nodos_sucesores) -1
    while(x >= 0 ):
        if nodos_sucesores[x][0] == nodo[0] and nodos_sucesores[x][1] == nodo[1]:
            print("Nodo", nodos_sucesores[x][0], "Nivel", nodos_sucesores[x][1])
            imprimir_papas(nodos_sucesores[x][2])
            break
        x = x -1

def esta_en_rango(x, y):
    return not (x < min_x or x > max_x or y < min_y or y > max_y)

def hay_alguien_alli(x, y, n):
    return n[x][y] != '0'

def movimiento(mov,c,xi,yi,n):
    if mov == 1:
        xf = xi - 2
        yf = yi + 1
    if mov == 2:
        xf = xi - 1
        yf = yi + 2
    if mov == 3:
        xf = xi + 1
        yf = yi + 2
    if mov == 4:
        xf = xi + 2
        yf = yi + 1
    if mov == 5:
        xf = xi + 2
        yf = yi - 1
    if mov == 6:
        xf = xi + 1
        yf = yi - 2
    if mov == 7:
        xf = xi - 2
        yf = yi - 1
    if mov == 8:
        xf = xi - 1
        yf = yi - 2
    if not esta_en_rango(xf, yf):
        return None
    if hay_alguien_alli(xf, yf, n):
        return None
    nodo_aux = deepcopy(n)
    nodo_aux[xi][yi] = '0'
    nodo_aux[xf][yf] = c
    return nodo_aux

def sucesores_limite(nodo):
    aux = nodo[0][:][:]
    np_nodo = np.array(aux)
    lr = []
    for c in caballos:
        indice = np.where(np_nodo == c)
        for q in range(1, 9):
            nodo_movimiento_c1 = movimiento(q, c,indice[0][0] ,indice[1][0] , nodo[0])
            (lr.append([nodo_movimiento_c1,nodo[1]+1]) if nodo_movimiento_c1 is not None else None)
            (nodos_sucesores.append([nodo_movimiento_c1, nodo[1] + 1,nodo]) if nodo_movimiento_c1 is not None else None)
            nodo_movimiento_c2 = movimiento(q, c, indice[0][1] ,indice[1][1] , nodo[0])
            (lr.append([(nodo_movimiento_c2),nodo[1]+1]) if (nodo_movimiento_c2) is not None else None)
            (nodos_sucesores.append([nodo_movimiento_c2, nodo[1] + 1,nodo]) if nodo_movimiento_c2 is not None else None)
    return lr

##############################################################################################
##############################################################################################
######################### A L G O R I T M O S   N  O   I N F O R M A D O S ###################
##############################################################################################
##############################################################################################

#anchura
def anchura_grafo_nivel(nodo_inicio, nodo_fin):
    lista = [[nodo_inicio, 0]]
    destapados = []
    c = 1
    while lista:
        nodo_actual = lista.pop(0)
        destapados.append(deepcopy(nodo_actual[0]))
        print('Nodo actual:', nodo_actual, "Contador:", c)
        c = c + 1
        if (nodo_actual[0] == nodo_fin):
            print("********************************************************************************************")
            print("************************ A N C H U R A   G R A F O *****************************************")
            print("Numero de nodos visitados: ", c-1)
            print("Niveles del arbol: ", nodo_actual[1])
            print("Numero de nodos en lista: ", len(lista))
            print("Numero de nodos en total: ",(c - 1) + len(lista))
            print("PAPAS:")
            imprimir_papas(nodo_actual)
            print("********************************************************************************************")
            return print("SOLUCION")
        temp = sucesores_limite(nodo_actual)
        if temp:
            x = [t for t in temp if t not in lista and t[0] not in destapados]
            lista.extend(deepcopy(x))
    print("NO SOLUCION")

#profundidad
def profundidad_grafo_nivel(nodo_inicio, nodo_fin):
    lista = [[nodo_inicio, 0]]
    destapados = []
    c = 1
    while lista:
        nodo_actual = lista.pop(0)
        destapados.append(deepcopy(nodo_actual[0]))
        print ('Nodo actual:', nodo_actual, "Contador:",c)
        c = c + 1
        if(nodo_actual[0] == nodo_fin):
            print("********************************************************************************************")
            print("********************** P R O F U N D I D A D   G R A F O ***********************************")
            print("Numero de nodos visitados: ", c-1)
            print("Niveles del arbol: ", nodo_actual[1])
            print("Numero de nodos en lista: ", len(lista))
            print("Numero de nodos en total: ",(c - 1) + len(lista))
            print("********************************************************************************************")
            return print("SOLUCION")
        temp = sucesores_limite(nodo_actual)
        if temp:
            x = [t for t in temp if t not in lista and t[0] not in destapados]
            x.extend(deepcopy(lista))
            lista = x
    print ("NO SOLUCION")

#costo_uniforme
def costo_uniforme_grafo(nodo_inicio, nodo_fin):
    lista = [[nodo_inicio, 0]]
    destapados = []
    c = 1
    while lista:
        nodo_actual = lista.pop(0)
        destapados.append(deepcopy(nodo_actual[0]))
        print('Nodo actual:', nodo_actual, "Contador:", c)
        c = c + 1
        if(nodo_actual[0] == nodo_fin):
            print("********************************************************************************************")
            print("************ C O S T O   U N I F O R M E   G R A F O ***************************************")
            print("Numero de nodos visitados: ", c -1)
            print("Niveles del arbol: ", nodo_actual[1])
            print("Numero de nodos en lista: ", len(lista))
            print("Numero de nodos en total: " ,(c-1)+len(lista))
            print("PAPAS:")
            imprimir_papas(nodo_actual)
            print("********************************************************************************************")
            return print ("SOLUCION")
        temp = sucesores_limite(nodo_actual)
        if temp:
            x = [t for t in temp if t not in lista and t[0] not in destapados]
            lista.extend(deepcopy(x))
            lista = sorted(lista ,key=lambda y: y[1])
    print ("NO SOLUCION")

##############################################################################################
##############################################################################################
##########################   E J E C U C I O N   #############################################
##############################################################################################
##############################################################################################

def output_anchura(nodo_inicio, nodo_fin):
    nodos_sucesores = []
    i = time.time()*1000
    anchura_grafo_nivel(nodo_inicio,nodo_fin)
    f = time.time()*1000
    delta = f - i
    print("TIEMPO DEL METODO",delta,"ms")

def output_profundidad(nodo_inicio, nodo_fin):
    nodos_sucesores = []
    i = time.time() * 1000
    profundidad_grafo_nivel(nodo_inicio, nodo_fin)
    f = time.time() * 1000
    delta = f - i
    print("TIEMPO DEL METODO", delta, "ms")

def output_costo_uniforme(nodo_inicio,nodo_fin):
    nodos_sucesores= []
    i = time.time() * 1000
    costo_uniforme_grafo(nodo_inicio, nodo_fin)
    f = time.time() * 1000
    delta = f - i
    print("TIEMPO DEL METODO", delta, "ms")

def algoritmos():
    while(True):
        print("Seleccione el algoritmo a ejecutar")
        print("1. Anchura grafo")
        print("2. Profundidad grafo")
        print("3. Costo Uniforme grafo ")
        print("4. Salir")
        option = input("opcion:")
        if int(option) == 1 :
            output_anchura(nodo_inicio,nodo_fin)
        elif int(option) == 2:
            output_profundidad(nodo_inicio, nodo_fin)
        elif int(option) == 3:
            output_costo_uniforme(nodo_inicio,nodo_fin)
        elif int(option) == 4:
            break

algoritmos()
