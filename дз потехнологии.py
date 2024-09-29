a = int(input('a = '))
b = int(input('b = '))

a, b = b, a + b - b
print(a, b)
