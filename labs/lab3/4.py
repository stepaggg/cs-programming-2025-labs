m = []
x = int(input('Введите число : '))
for  y in range(1,x):
    x *= y
    m.append(x)
print(m)