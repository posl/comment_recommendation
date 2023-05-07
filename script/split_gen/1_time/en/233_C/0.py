def main():
    N, X = map(int, input().split())
    L = []
    A = []
    for _ in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    ans = 0
    for i in range(2**N):
        p = 1
        for j in range(N):
            if (i >> j) & 1:
                p *= A[j][0]
            else:
                p *= A[j][1]
        if p <= X:
            ans += 1
    print(ans)
