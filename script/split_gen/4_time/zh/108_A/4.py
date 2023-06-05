def fun(k):
    sum=0
    for i in range(1,k+1):
        if i%2==0:
            for j in range(1,k+1):
                if j%2==1:
                    sum+=1
    return sum
k=int(input())
print(fun(k))
