def lllsk(K):
    if K<10:
        return K
    else:
        K-=10
        a=1
        while K>0:
            a+=1
            if a<10:
                K-=1
            else:
                K-=2
        if K==0:
            return a
        else:
            return int(str(a)+str(a+1))
K=int(input())
print(lllsk(K))
