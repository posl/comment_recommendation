def main():
    N, X = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    ans = 0
    for i in range(1, 2**N):
        b = 0
        for j in range(N):
            if i >> j & 1:
                b += L[j]
        if b > X:
            continue
        for j in range(1, 2**b):
            c = 1
            for k in range(b):
                if j >> k & 1:
                    c *= A[k].pop()
            if c == X:
                ans += 1
    print(ans)
