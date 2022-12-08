from sys import stdin
input = stdin.readline

r_c = input().split()
r, c = int(r_c[0]), int(r_c[1])
# Matrix = [[0 for x in range(w)] for y in range(h)] 
Matrix = [[]*r]*c
for i in range(r):
    data = input().split()
    for k in range(c):
        Matrix[i].append(int(data[k]))
print(Matrix)
