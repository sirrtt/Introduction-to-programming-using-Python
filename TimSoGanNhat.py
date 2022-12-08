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
    list_after = []
    l = findCrossOver(arr, 0, n - 1, x)
    r = l + 1 
    count = 0 
    if (arr[l] == x) :
        list_after.append(arr[l])
        l -= 1
        count += 1
        while (l >= 0 and r < n and count < k) :
            if (x - arr[l] < arr[r] - x) :
                list_after.append(arr[l])
                l -= 1
            else :
                list_after.append(arr[l])
                l -= 1
            count += 1
    while (l >= 0 and r < n and count < k) :
        if (x - arr[l] < arr[r] - x) :
            list_after.append(arr[l])
            l -= 1
        else :
            list_after.append(arr[r])
            r += 1
        count += 1
    while (count < k and l >= 0) :
        list_after.append(arr[l])
        l -= 1
        count += 1
    while (count < k and r < n) :
        list_after.append(arr[r])
        r += 1
        count += 1
    list_after.sort()
    for i in list_after:
        print(i, end=" ")
        
if __name__ == "__main__" :
    n = int(input())
    list = []
    list = input().split()
    res = [eval(i) for i in list]          
    k_x = input().split()
    k = int(k_x[0])
    x = int(k_x[1])
    printKclosest(res, x, k, len(res))