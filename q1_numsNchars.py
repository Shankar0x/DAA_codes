def movearound(intarr,chararr,res):
    if len(intarr)>1:
        mid1 = len(intarr)//2
        a1 = intarr[:mid1]
        a2 = intarr[mid1:]
        mid2 = len(chararr)//2
        b1 = chararr[:mid2]
        b2 = chararr[mid2:]

        movearound(a1,b1,res)
        movearound(a2,b2,res)
    else:
        res.append(intarr[0])
        res.append(chararr[0])

arr = [1,2,3,4,5,'a','b','c','d','e']
mid = len(arr)//2
res = []
movearound(arr[:mid],arr[mid:],res)
print(res)
