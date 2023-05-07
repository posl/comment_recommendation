def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    #print(N, X)
    #print(L)
    ans = 0
    for i in range(2**N):
        a = [0 for j in range(N)]
        for j in range(N):
            if (i >> j) & 1:
                a[j] = 1
        #print(a)
        tmp = 1
        for j in range(N):
            if a[j] == 1:
                tmp *= L[j][a[j]]
        if tmp == X:
            ans += 1
    print(ans)
