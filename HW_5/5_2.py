def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a ^ b, (a & b) << 1)

a = int(input())
b = int(input())
print(sum(a, b))