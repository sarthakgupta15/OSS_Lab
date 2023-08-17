def duplicates(list):
    l1=[]
    for i in list:
        if i not in l1:
            l1.append(i)
        else:
            print(i,end=' ')

l=[1,2,3,4,5,2,3,4,7,9,5]
duplicates(l)
print("\n")