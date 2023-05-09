def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    AB = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        AB.append(a + b)
    AB.sort()
    ans = 0
    for i in range(N):
        if i < X:
            ans += AB[i]
        else:
            ans += B[i]
    print(ans)
