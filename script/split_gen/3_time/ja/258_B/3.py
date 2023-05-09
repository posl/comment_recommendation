def solve():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, list(input()))))
    ans = 0
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp = tmp * 10 + A[(i + k) % N][(j + k) % N]
            ans = max(ans, tmp)
    print(ans)
