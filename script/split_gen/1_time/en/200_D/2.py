def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    d = [[] for i in range(mod)]
    for i in range(N):
        d[A[i] % mod].append(i + 1)
    for i in range(mod):
        if len(d[i]) >= 2:
            print("Yes")
            print(1, d[i][0])
            print(1, d[i][1])
            return
    for i in range(mod):
        for j in range(i + 1, mod):
            if len(d[i]) >= 1 and len(d[j]) >= 1:
                print("Yes")
                print(2, d[i][0], d[j][0])
                print(1, d[i][0] if d[i][0] < d[j][0] else d[j][0])
                return
    print("No")
