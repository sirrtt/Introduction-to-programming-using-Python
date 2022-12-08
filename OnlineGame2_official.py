# from sys import stdin
# input = stdin.readline

# status_dict = {}
# while (True):        
#     com_data = list(map(int, input().split()))
#     if len(com_data) == 0:
#         break
#     elif com_data[0]==1:
#         status_dict.update({com_data[1]: 0})
#     elif com_data[0]==3:
#         if status_dict.get(com_data[1]) == 0:
#             status_dict.pop(com_data[1])
#     elif com_data[0]==2:
#         if status_dict.get(com_data[1]) == 0:
#             print(1)
#         else:
#             print(0)
#     else:
#         break

from sys import stdin
input = stdin.readline

mainset = set()
while (True):
    com_data = list(map(int, input().split()))
    if com_data[0] == 0:
        break
    elif com_data[0] == 1:
        mainset.add(com_data[1])
    elif com_data[0] == 3:
        mainset.discard(com_data[1])
    elif com_data[0] == 2:
        if com_data[1] in mainset:
            print(1)
        else:
            print(0)