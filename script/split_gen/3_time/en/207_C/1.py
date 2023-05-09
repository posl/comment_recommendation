def main():
    N = int(input())
    T = []
    L = []
    R = []
    for i in range(N):
        t, l, r = map(int, input().split())
        T.append(t)
        L.append(l)
        R.append(r)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if T[i] == 1:
                p = L[i]
            elif T[i] == 2:
                p = L[i] + 1
            elif T[i] == 3:
                p = R[i] - 1
            else:
                p = R[i]
            if T[j] == 1:
                q = L[j]
            elif T[j] == 2:
                q = L[j] + 1
            elif T[j] == 3:
                q = R[j] - 1
            else:
                q = R[j]
            if p <= q:
                ans += 1
    print(ans)
