cattle_number, legs = list(map(int,input().split()))
chickens = (legs - 4 * cattle_number) // -2
dogs = cattle_number - chickens
print(str(chickens) + ' ' + str(dogs))