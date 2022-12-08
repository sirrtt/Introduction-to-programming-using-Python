station, time = map(int,input().split())
way = time//station
if way % 2 != 0:
    station = station * (way + 1)
    out = station - time
    print(out)
else:
    out = time % station
    print(out)