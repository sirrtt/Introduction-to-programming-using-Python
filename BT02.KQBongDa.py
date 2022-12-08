import array
class Soccer:
    def __init__(self, won, lost, yellow_card):
        self.won = won
        self.lost = lost
        self.yellow_card = yellow_card

a = [None] * 3
b = [None] * 3

def main():
    for i in range(3):
        won, lost, yellow_card = list(map(int,input().split()))
        a[i] = Soccer(won, lost, yellow_card)
    for i in range(3):
        won, lost, yellow_card = list(map(int,input().split()))
        b[i] = Soccer(won, lost, yellow_card)
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    for i in range(3):
        if a[i].won - a[i].lost > 0:
            a1 = a1 + 3
        elif a[i].won - a[i].lost == 0:
            a1 = a1 + 1

        a2 = a2 + (a[i].won - a[i].lost)
        a3 = a3 + a[i].won
        a4 = a4 + a[i].yellow_card    

        if b[i].won - b[i].lost > 0:
            b1 = b1 + 3
        elif b[i].won - b[i].lost == 0:
            b1 = b1 + 1
        
        b2 = b2 + b[i].won - b[i].lost
        b3 = b3 + b[i].won
        b4 = b4 + b[i].yellow_card

    if a1 >= b1 and a2 > b2 and a3 > b3 and a4 < b4:
        print(str(a1)+" "+str(a2)+" "+str(a3)+" "+str(a4))
    elif a1 > b1 and a2 >= b2:
        print(str(a1)+" "+str(a2)+" "+str(a3)+" "+str(a4))
    elif a1 > b1 and a3 >= b3:
        print(str(a1)+" "+str(a2)+" "+str(a3)+" "+str(a4))
    else:
        print(str(b1)+" "+str(b2)+" "+str(b3)+" "+str(b4))
main()