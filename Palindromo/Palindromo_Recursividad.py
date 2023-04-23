def es_palindromo_recursivo(palabra):
    palabra = palabra.lower().replace(" ", "")
    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo_recursivo(palabra[1:-1])
    else:
        return False