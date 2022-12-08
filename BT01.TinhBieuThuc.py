import math

a, b, c = list(map(float,input().split()))
x = a ** 5 - 2 * math.sqrt(abs(b)) + a * b * c
print(format(x, ".2f"))
