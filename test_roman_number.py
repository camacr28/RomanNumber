from roman_funcs import arabic_to_roman, divide_en_miles, dividir_en_digitos, to_roman


def test_romanos_simples():
    assert to_roman(1) == 'I'
    assert to_roman(5) == 'V'
    assert to_roman(10) == 'X'
    assert to_roman(50) == 'L'
    assert to_roman(100) == 'C'
    assert to_roman(500) == 'D'
    assert to_roman(1000) == 'M'


def test_romanos_1_al_9():
    assert to_roman(1) == 'I'
    assert to_roman(2) == 'II'
    assert to_roman(3) == 'III'
    assert to_roman(4) == 'IV'
    assert to_roman(5) == 'V'
    assert to_roman(6) == "VI"
    assert to_roman(7) == 'VII'
    assert to_roman(8) == 'VIII'
    assert to_roman(9) == 'IX'


def test_romanos_10_al_90():
    assert to_roman(10) == 'X'
    assert to_roman(20) == 'XX'
    assert to_roman(30) == 'XXX'
    assert to_roman(40) == 'XL'
    assert to_roman(50) == 'L'
    assert to_roman(60) == "LX"
    assert to_roman(70) == 'LXX'
    assert to_roman(80) == 'LXXX'
    assert to_roman(90) == 'XC'


def test_romanos_100_al_1000():
    assert to_roman(100) == 'C'
    assert to_roman(200) == 'CC'
    assert to_roman(300) == 'CCC'
    assert to_roman(400) == 'CD'
    assert to_roman(500) == 'D'
    assert to_roman(600) == 'DC'
    assert to_roman(700) == 'DCC'
    assert to_roman(800) == 'DCCC'
    assert to_roman(900) == 'CM'
    assert to_roman(1000) == 'M'


def test_dividir_en_digitos():
    assert dividir_en_digitos(34) == [0, 0, 30, 4]
    assert dividir_en_digitos(100) == [0, 100, 0, 0]
    assert dividir_en_digitos(2024) == [2000, 0, 20, 4]


def test_conversion():
    assert arabic_to_roman(970) == 'CMLXX'
    assert arabic_to_roman(1999) == 'MCMXCIX'
    assert arabic_to_roman(2024) == 'MMXXIV'
    assert arabic_to_roman(34) == 'XXXIV'
    assert arabic_to_roman(100) == 'C'
    assert arabic_to_roman(3999) == 'MMMCMXCIX'
    assert arabic_to_roman(1902) == 'MCMII'


def test_romano_mayor_3999():
    assert arabic_to_roman(4127) == 'IV*CXXVII'
    assert arabic_to_roman(3956412) == 'MMMCMLVI*CDXII'
    assert arabic_to_roman(4956412) == 'IV**CMLVI*CDXII'
    na = int(6.022e23)
    assert arabic_to_roman(na) == "DCII*******CC******XXVII**CCLXII*CMLXXVI"


def test_divide_en_miles():
    assert divide_en_miles(4127) == [127, 4]
    assert divide_en_miles(3127) == [3127]


def test_divide_en_miles_pero_con_millones():
    assert divide_en_miles(4123234) == [234, 123, 4]
    assert divide_en_miles(3123234) == [234, 3123]
