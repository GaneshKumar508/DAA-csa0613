a=[64,25,12,22,11]
l=len(a)
for i in range(l):
    for i+1 in range(l):
        if(a[i]<a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]
print(a)
