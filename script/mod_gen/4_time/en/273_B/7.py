def calc(X,K):
    if X==0:
        return 0
    else:
        return int(str(X)[0:K]+'0'*(len(str(X))-K))
X,K = [int(i) for i in input().split()]
print(calc(X,K))
