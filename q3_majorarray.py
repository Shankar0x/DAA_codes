def majorelem(arr,l,r):
    if l == r-1:
        return arr[l],1
    mid = l + ((r-l)//2)
    maj_left,extra_left = majorelem(arr,l,mid)
    maj_right, extra_right = majorelem(arr,mid,r)

    if maj_left == maj_right:
        maj = maj_left
        extra = extra_left+extra_right
    elif extra_right > extra_left:
        maj = maj_right
        extra = extra_right - extra_left
    else:
        maj = maj_left
        extra = extra_left - extra_right
    return maj,extra

if __name__ == '__main__':
    arr = [1,1,1,1,1,2,2,2,2,2,2,2,2]
    ans,_ = majorelem(arr,0,len(arr)-1)
    print(f"Majority element is: {ans}")