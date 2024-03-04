# módulo para organizar funciones o clases utilizadas en nuestro proyecto

#Funcion fibo
def fibo(n):
    if n in {0,1}:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    


