def group(list,size):
    i=0
    r=[]
    temp=[]
    for item in list:
        if i<size:
            i+=1
            temp.append(item)
        if i==size:
            r.append(temp)
            i=0
            temp.clear()
    print(r)
    return r

l=[1,2,3,4,5,6,7,8,9]
group(l,3)