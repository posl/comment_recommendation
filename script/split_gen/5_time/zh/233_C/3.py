def f(L, X):
    #print(L, X)
    if len(L) == 1:
        if X in L[0]:
            return 1
        else:
            return 0
    else:
        a = L[0]
        b = L[1:]
        c = []
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(b[j])):
                    if a[i] * b[j][k] <= X:
                        c.append(a[i] * b[j][k])
        return f([c] + L[2:], X)
N, X = map(int, input().split())
L = []
for i in range(N):
    L.append(list(map(int, input().split()[1:])))
print(f(L, X))
