import array
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if a[i] > 2:
        if a[i] % 2 == 0:
            print(0)
        else:
            b = a[i] + 1 - a[i]
            print(b)
    else:
        b = a[i] + 2 - a[i]
        print(b)