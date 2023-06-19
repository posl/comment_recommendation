def dice(a,b):
    for i in range(1,7):
        for j in range(1,7):
            if i+j==b and a==2:
                return 'Yes'
    return 'No'
a,b=map(int,input().split())
print(dice(a,b))
