list=[64,25,12,22,11]
l=len(list)
for i in range(l):
    for j in range(l):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
