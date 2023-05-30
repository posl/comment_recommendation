def takoyaki():
    N,X,T = map(int, input().split())
    if N % X == 0:
        return (N//X)*T
    else:
        return (N//X + 1)*T
print(takoyaki())
