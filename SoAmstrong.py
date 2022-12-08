K = input()
i=0
sum=0
for i in range(len(K)):
    sum=sum+pow(int(K[i]), len(K))
if (sum==int(K)):
    print('True')
else: 
    print('False')

