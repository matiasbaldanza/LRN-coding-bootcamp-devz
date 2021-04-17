# Ejercicio 1: 
# Escribe un programa que verifique que una frase es un palíndromo.
# Un palíndromo es una frase que se lee igual de derecha a izquierda que de izquierda a derecha.

# In: “La ruta nos aportó otro paso natural”
# Out: true

# In: “Claramente, esto no es un palíndromo”
# Out: false

# V1: Por comparación de subcadenas.
# Problemas: No contempla el uso de caracteres acentuados

def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(' ', '')
    longitud = len(texto)
    if longitud %2 == 0:
        parte_izquierda = texto[:longitud // 2]
        parte_derecha = texto[longitud // 2:]
    else:
        parte_izquierda = texto[:longitud //2]
        parte_derecha = texto[longitud //2 + 1:]
    return parte_izquierda == parte_derecha[::-1]

print(es_palindromo('Dabale arroz a la zorra el abad'))
print(es_palindromo('La ruta nos aporto otro paso natural'))
print(es_palindromo('Claramente esto no es un palindromo'))

