n = int(input())
sum = 0
for i in range(1, n):
    k=n%i
    if k==0 and k!=n:
        sum=sum+i
print(sum)
