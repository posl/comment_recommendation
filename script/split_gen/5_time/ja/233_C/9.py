def main():
    N, X = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    ans = 0
    for i in range(N):
        if len(A[i]) == 1:
            if X % A[i][0] == 0:
                ans += 1
        else:
            for j in range(L[i]):
                if X % A[i][j] == 0:
                    ans += 1
    print(ans)
