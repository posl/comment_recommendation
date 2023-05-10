def f(K,X):
    result = []
    for i in range(X-K+1,X+K):
        result.append(str(i))
    return " ".join(result)
K,X = map(int,input().split())
print(f(K,X))
