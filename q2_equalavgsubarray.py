def parto(arr,l,r):
    mid = (r-l)//2
    lavg = sum(arr[l:mid])/len(arr[l:mid])
    ravg = sum(arr[mid:r+1])/len(arr[mid:r+1])

    if lavg == ravg:
        return mid
    elif lavg > ravg:
        lavg = sum(arr[l:(mid-l)//2])/len(arr[l:(mid-l)//2])
        ravg = sum(arr[(mid-l)//2:r+1])/len(arr[(mid-l)//2:r+1])
        parto(arr,)
    else:
        lavg = sum(arr[l:((r+1)-(mid+1))//2])/len(arr[l:((r+1)-(mid+1))//2])
        ravg = sum(arr[((r+1)-(mid+1))//2,r+1])/len(arr[((r+1)-(mid+1))//2,r+1])
print(parto([5,4,3,1,9,2],0,5))