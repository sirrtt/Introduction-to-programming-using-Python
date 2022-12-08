from curses import has_colors


def make_2d_list(w, h):
    return [[0] * h for i in range(w)]

def set_2d_list(list_2d):
    n = len(list_2d)
    list_Length = [0] * len(list_2d[0])
    for i in range(n):
        row = list(map(int,input().split()))
        list_2d[i] = row
        for j in range(len(row)):
            list_Length[j] = max(list_Length[j],len(str(row[j])))
    return list_Length

def print_2d_list(list_2d, list_Length):
    n = len(list_2d)
    for row in list_2d:
        for i in range(len(row)):
            if i != (len(row) - 1):
                print(str(row[i]).rjust(list_Length[i]),end = ' ')
            else:
                print(str(row[i]).rjust(list_Length[i]))

w, h = map(int,input().split())
list_2d = make_2d_list(w, h)
list_Length = set_2d_list(list_2d)
print_2d_list(list_2d, list_Length)