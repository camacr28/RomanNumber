valors = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}


def to_roman(n):

    if n in valors:
        result = valors[n]
    elif n <= 3:
        result = n * valors[1]
    elif n == 4:
        result = valors[1] + valors[5]
    elif n < 9:
        result = valors[5] + (n - 5) * valors[1]
    elif n == 9:
        result = valors[1] + valors[10]
    elif n <= 30:
        result = (n//10) * valors[10]
    elif n == 40:
        result = valors[10] + valors[50]
    elif n < 90:
        result = valors[50] + ((n//10) - 5) * valors[10]
    elif n == 90:
        result = valors[10] + valors[100]
    else:
        result = valors[n]

    return result
