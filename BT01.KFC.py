DoF = float(input())
DoC = (DoF - 32)/1.8
DoK = DoC + 273.15
print(str(format(DoC, "g"))+' '+str(format(DoK, "g")))