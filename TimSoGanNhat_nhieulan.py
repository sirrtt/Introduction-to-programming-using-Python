def findCrossOver(arr, low, high, x) :
    if (arr[high] <= x) : 
        return high
    if (arr[low] > x) : 
        return low
    mid = (low + high) // 2 
    if (arr[mid] == x and arr[mid + 1] > x) :
        return mid
    if(arr[mid] < x) :
        return findCrossOver(arr, mid + 1, high, x)
    return findCrossOver(arr, low, mid - 1, x)
 
def printKclosest(arr, x, k, n) :
    i = findCrossOver(arr, 0, n - 1, x)
    l, r = 1, 1 
    count = 0 
    for ind in range(k-1):
        if i-l > -1 and i+r < n:
            if (x - arr[i-l] <= arr[i+r] - x):
                l+=1
            else:
                r+=1
        elif i-l>-1:
            l+=1
        elif i+r<n:
            r+=1
    return arr[i-l+1], arr[i+r-1]
        
if __name__ == "__main__" :
    n = int(input())
    list = []
    d=[]
    list = input().split()
    res = [eval(i) for i in list]   
    while (True):        
        k_x = input()
        if k_x=="":
            break
        k_x = k_x.split()
        k = int(k_x[0])
        x = int(k_x[1])
        d.append(printKclosest(res, x, k, len(res)))
    for i in d:
        print(f'{i[0]} {i[1]}')