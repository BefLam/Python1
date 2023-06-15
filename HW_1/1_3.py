n = int(input("Введите шестизначное число: "))

m1 = n // 100000
m2 = n // 10000 % 10
m3= n // 1000 % 10
n1= n // 100 % 10
n2= n // 10 % 10
n3= n % 10
a = m1+m2+m3
b = n1+n2+n3

if a == b:
    print ('Yes')
else:
    print ('No')



