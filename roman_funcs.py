values = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}


def to_roman(n):

    order, d = calc_d_order(n)

    if d <= 3:
        result = d * values[order]
    elif d == 4:
        result = values[order] + values[5*order]
    elif d < 9:
        result = values[5*order] + (d - 5) * values[order]
    elif d == 9:
        result = values[order] + values[10*order]

    return result


def calc_d_order(n):
    order = 10**(len(str(n))-1)
    d = n//order
    return order, d


def dividir_en_digitos(n: int):
    lista_nums = []
    cad = f'{n:04d}'
    mult = 1000

    for digito in cad:
        lista_nums.append(int(digito) * mult)
        mult //= 10

    return lista_nums


def digits_to_roman(lista_nums: list):
    result = ''
    for num in lista_nums:
        result += to_roman(num)

    return result


def arabic_to_roman(n: int):
    miles = divide_en_miles(n)
    result = ''
    for num_asteriscos, cifra in enumerate(miles):
        lista = dividir_en_digitos(cifra)
        romano = digits_to_roman(lista)
        if romano != '':
            romano += '*' * num_asteriscos
        result = romano + result

    return result


def divide_en_miles(n: int):
    lista_nums = []
    modulo = n % 1000
    entero = n//1000

    while entero > 999:
        lista_nums.append(modulo)
        n = entero
        modulo = entero % 1000
        entero = entero // 1000

    if entero < 4:
        lista_nums.append(n)
    else:
        lista_nums.append(modulo)
        lista_nums.append(entero)

    return lista_nums
