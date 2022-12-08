from sys import stdin
import queue

arr = []
prique_remove = queue.PriorityQueue()
que = queue.Queue()
while (True):
    input = stdin.readline().split()
    if input[0] == '5':
        if len(arr) == 0:
            continue
        else:
            arr.remove(arr[0])
    elif input[0] == '4':
        for i in range(arr.count(input[1])):
            arr.remove(input[1])
    elif input[0] == '3':
        if arr.count(input[1]) == 0:
            pass
        else:
            arr.remove(input[1])
    elif input[0] == '2':
        if arr.count(input[1]) == 0:
            location = -1
        else:
            location = arr.index(input[1])
        arr.insert(location + 1, input[2])
    elif input[0] == '1':
        arr.append(input[1])
    elif input[0] == '0':
        arr.insert(0, input[1])
    else:
        break
if len(arr)!=0:
    for i in arr:
        print(i, end=' ')
else:
    print('blank')