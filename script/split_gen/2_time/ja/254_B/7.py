def pascal(N):
    if N==0:
        return [1]
    elif N==1:
        return [1,1]
    else:
        return [1]+[pascal(N-1)[i]+pascal(N-1)[i+1] for i in range(N-1)]+[1]
N=int(input())
for i in range(N):
    print(*pascal(i))
N=int(input())
for i in range(N):
    print(*[1]+[pascal(N-1)[i]+pascal(N-1)[i+1] for i in range(N-1)]+[1])
