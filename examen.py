''''
Hacemos una función para ser reutilizada en caso de futuros cambios,
donde validaremos si en la lista hay 2 números que sumados den X.
La lista es un bucle anidado, O(n^2) porque si tenemos 10 elementos
en el arreglo, en el 2do bucle se itera por lo mismos elementos
seria un 10^2 = 100 iteraciones mas o menos, el valor en si no cambia
la complejidad. Porque esta haciendo fuerza bruta en este algoritmo 
'''

def sum_elements_for(list_num,sum):
    for i in range(len(list_num)):
        for j in range(i + 1, len(list_num)):
            if(list_num[i]+list_num[j]  == sum):
                return True
    return False

'''
En este algoritmo, más optimizado, tenemos una complejidad O(n) porque
solo es una iteración. Con un uso de memoria para comparar, usamos
un SET para no repetir números, un solo for, y la verificación
si podemos encontrar la diferencia del número, ejemplo sencillo
Queremos encontrar la suma entre 2 números de 8, entonces en la 1era
iteración, el valor del indice 0, es 3, entonces se busca la diferencia
entre 8-3 = 5, entonces 5 existe en el set? En este caso NO,
En el caso de encontrar esa diferencia, podemos retornar True
Porque si existen 2 números que suman el número que buscamos.
'''
def sum_elements_set(list_num, sum):
    numeros_iterados = set()  
    for num in list_num:
        diff = sum - num
        if diff in numeros_iterados:  
            return True
        numeros_iterados.add(num)  
    return False

'''
En este algoritmo le damos un enfoque mas a una busqueda binaria,
donde primero debemos ordenar la lista, tiene una complejidad
O(n log n) por el ordenamiento del sort(). Sino seria O(log n).
Primero ordenamos el arreglo, left indica el primer elemento
del arreglo, y right el ultimo elemento.
Hacemos un bucle con condicion mientras left sea menor a right,
guardamos el valor actual de la suma de los 2 elementos.
Y en las condiciones, validamos si el número es menor o mayor
al número que buscamos, le restamos -1 al valor de right, y si
es menor, le sumamos +1 al de left. Ejemplo buscamos 2 números
que sumados den 8, left es de valor 1 y right valor 8, 
resultado = 9, 9 es igual a 8?, es superior, entonces right -1,
1 + 7 = 8¿ SI, lo encontramos.
'''
def sum_elements_binary(list_num, requiredSum):
    list_num.sort()  
    left, right = 0, len(list_num) - 1 # asignación multiple

    while left < right:
        current_sum = list_num[left] + list_num[right]
        if current_sum == requiredSum:
            return True
        elif current_sum < requiredSum:
            left += 1 
        else:
            right -= 1 
    return False


requiredSum = 8
nums = [1,4,3,9]

print(sum_elements_for(nums,requiredSum))

print(sum_elements_set(nums, requiredSum))  

print(sum_elements_binary(nums, requiredSum))  




