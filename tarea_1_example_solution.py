
""""Metodo recibe un dato de entrada base
    Switch case" mediante if y elif, determina condiciones de error:
    variable booleana, tipo NoneType,
    numero decimal, string de caracteres y mayor a 100.
    Cada caso de error retorna un codigo específico y un valor nulo
    Si no, recorre lista de primos hasta el dato de entrada
    y retorna un codigo de exito y el arreglo de numeros primos"""


def invert_case(cadena):
    # Verifica que la entrada sea un string
    if type(cadena) is not str:
        return -16, None

    # Ciclo que va revisando cada caracter de la entrada pertenezca al alfabeto
    for caracter in cadena:
        if not ('a' <= caracter <= 'z' or 'A' <= caracter <= 'Z'):
            return -32, None

    # Veriffica que la entrada no este vacia
    if len(cadena) == 0:
        return -48, None

    # Ciclo que convierte mayuscula a minuscula y viceversa
    nueva_cadena = ""
    for caracter in cadena:
        if caracter.islower():
            nueva_cadena += caracter.upper()
        else:
            nueva_cadena += caracter.lower()
    return 0, nueva_cadena


def numero_primo(base):
    # Lista de numeros primos entre 0 y 100, ya que son pocos
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if type(base) is not int:
        return -64, None
    elif type(base) is int and base > 100:
        return -80, None
    else:
        i = 0
        # Ciclo para obtener los numeros primos antes del numero dado
        # If para evitar IndexError si dato es mayor a ultimo numero primo
        while primos[i] <= base:
            i += 1
            if i == len(primos):
                break
        return 0, primos[0:i]
