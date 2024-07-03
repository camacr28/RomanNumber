values = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}


def to_roman2(n):

    if n in values:
        result = values[n]
    elif n <= 3:
        result = n * values[1]
    elif n == 4:
        result = values[1] + values[5]
    elif n < 9:
        result = values[5] + (n - 5) * values[1]
    elif n == 9:
        result = values[1] + values[10]
    elif n <= 30:
        result = (n//10) * values[10]
    elif n == 40:
        result = values[10] + values[50]
    elif n < 90:
        result = values[50] + (n//10 - 5) * values[10]
    elif n == 90:
        result = values[10] + values[100]
    elif n <= 300:
        result = (n//100) * values[100]
    elif n == 400:
        result = values[100] + values[500]
    elif n < 900:
        result = values[500] + (n//100 - 5) * values[100]
    elif n == 900:
        result = values[100] + values[1000]

    return result


def to_roman(n):

    order = 10**(len(str(n))-1)
    d = n//order

    if d <= 3:
        result = d * values[order]
    elif d == 4:
        result = values[order] + values[5*order]
    elif d < 9:
        result = values[5*order] + (d - 5) * values[order]
    elif d == 9:
        result = values[order] + values[10*order]

    return result


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
    lista = dividir_en_digitos(n)
    return digits_to_roman(lista)
