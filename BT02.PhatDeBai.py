n = int(input())
k = int(input())
p = int(input())
q = int(input())
pos = 2*(p-1)+q
if pos-k > 0:
    posBob = pos-k
    if (posBob%2==0):
        posBob = 2
    else:
        posBob = 1
    row = (pos - k - posBob) // 2 + 1
    print(str(row)+" "+str(posBob))
elif pos+k <= n:
    posBob = pos+k
    if (posBob%2==0):
        posBob = 2
    else:
        posBob = 1
    row = (pos + k - posBob) // 2 + 1
    print(str(row)+" "+str(posBob))
else:
    print(-1)
