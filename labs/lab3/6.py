n = int((input('введите число: ')))
fib = []
a = 0
b = 1
while a <= n:
    fib.append(a)
    s = a
    a = b
    b = s + b
print('числа фиббоначи до ',n,':', fib)
