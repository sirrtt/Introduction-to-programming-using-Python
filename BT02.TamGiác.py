import math
a = float(input())
b = float(input())
c = float(input())
if a+b>c and b+c>a and a+c>b:
    P=(a+b+c)/2
    S=math.sqrt(P*(P-a)*(P-b)*(P-c))
    S='%g'%round(S, 2)
    a2=a**2
    b2=b**2
    c2=c**2
    if a==b==c:
        print(f'Tam giac deu, dien tich = {S}')
    elif a2==b2+c2 or b2==a2+c2 or c2==a2+b2:
        print(f'Tam giac vuong, dien tich = {S}')
    elif a==b or b==c or a==c:
        print(f'Tam giac can, dien tich = {S}')
    else:
        print(f'Tam giac thuong, dien tich = {S}')
else:
    print("Khong phai tam giac")