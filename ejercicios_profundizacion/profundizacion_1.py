# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
numero_1 = float(input("Ingrese primer numero: "))
numero_2 = float(input("Ingrese segundo numero: "))

print("Los numeros ingresado son:", numero_1 , numero_2)
suma = numero_1 + numero_2
print("el valor de la suma es:",suma)
resta_1 = numero_1 - numero_2
print("El valor de la resta del primer numero menos el segundo es:",resta_1)
resta_2 = numero_2 - numero_1
print("El valor de la resta del segundo numero menos el primero es:",resta_2)
multiplicacion = numero_1 * numero_2
print("El valor de la multiplicacion es: ", multiplicacion)
division_1 = numero_1 / numero_2
print("La division de los numeros es:", division_1)
pontncia = numero_1 ** numero_2
print("La potencia es:", pontncia)