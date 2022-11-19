def partition(arr,l,r):
    pivot = arr[r]
    i = l-1
    for j in range(l,r):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def qsort(arr,l,r):
    if (l<r):
        piv = partition(arr,l,r)
        qsort(arr,l,piv-1)
        qsort(arr,piv+1,r)

array = [10, 7, 8, 9, 1, 5]
qsort(array, 0, len(array) - 1)
  
print(f'Sorted array: {array}')