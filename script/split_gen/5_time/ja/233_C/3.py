def main():
    N,X = map(int,input().split())
    L = []
    A = []
    for i in range(N):
        L.append(list(map(int,input().split())))
    for i in range(N):
        A.append(L[i][1:])
    from itertools import product
    ans = 0
    for i in product(*A):
        if sum(i) == X:
            ans += 1
    print(ans)
