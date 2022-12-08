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
    list_after = [arr[i]]
    l, r = 1, 1 
    count = 0 
    for ind in range(k-1):
        if i-l > -1 and i+r < n:
            if (x - arr[i-l] <= arr[i+r] - x):
                list_after.append(arr[i-l])
                l+=1
            else:
                list_after.append(arr[i+r])
                r+=1
        elif i-l>-1:
            list_after.append(arr[i-l])
            l+=1
        elif i+r<n:
            list_after.append(arr[i+r])
            r+=1
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