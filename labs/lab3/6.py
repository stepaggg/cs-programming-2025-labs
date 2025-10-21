n = int((input('введите число: ')))
fib = []
a = 0
b = 1
while a <= n:
    fib.append(a)
    a = b
    b = a + b
print('числа фиббоначи до ',n,':', fib)
