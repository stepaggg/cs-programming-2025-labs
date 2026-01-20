input_string = input('введит 3 числаб разделенные запятыми:')
n = input_string.split(',')
a = int(n[0].strip())
b = int(n[1].strip())
c = int(n[2].strip())
s = (a+c)//b
print(f'результат вычисления {s}')