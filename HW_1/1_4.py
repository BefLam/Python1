n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))
k = int(input("Введите значение k: "))

if n * m >= k:
    if k % n == 0 or k % m == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
