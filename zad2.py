print(0.1 * 0.1)  # 0.010000000000000002

# Kod nie wyświetla 0,01, ponieważ nie wynaleziono
# jeszcze dokładnej reprezentacji liczb zmiennoprzecinkowych w
# postaci binarnej. Standard IEEE 754 nie zapewnia 100% dokładności.

# W przypadku precyzyjnych operacji wykorzystujących liczby
# zmiennoprzecinkowe należy użyć Decimal

from decimal import Decimal, ROUND_UP

print(Decimal('0.1') * Decimal('0.1'))  # 0.01

# Aby zaokrąglić liczby, można użyć funkcji round(), do której można przekazać
# określoną liczbę miejsc dziesiętnych jako drugi parametr
print(round(0.012802, 3))  # 0.013

# Aby dokładniej zaokrąglić liczby, można użyć metody quantize().

value = Decimal('0.010000000000000002')
rounded_value = value.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded_value)
