def partition(arr,l,r):
    x = arr[r]
    i = l
    for j in range(l,r):
        if arr[j]<=x:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    arr[r],arr[i] = arr[i],arr[r]
    return i

def qsel(arr,l,r,k):
    if (k > 0 and k <= r - l + 1):
        p = partition(arr,l,r)
        if p-l == k-1:
            return arr[p]
        elif p-l > k-1:
            return qsel(arr,l,p-1,k)
        else:
            return qsel(arr,p+1,r,k-p+l-1)
arr = [ 10, 4, 5, 8, 6, 11, 26 ]
n = len(arr)
k = 3
print("K-th smallest element is ", end = "")
print(qsel(arr, 0, n - 1, k))
