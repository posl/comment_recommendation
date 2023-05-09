def solve():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        x, y, z = map(int, input().split())
        cakes.append((x, y, z))
    ans = 0
    for i in range(2 ** 3):
        tmp = []
        for j in range(N):
            val = 0
            for k in range(3):
                if i >> k & 1:
                    val += cakes[j][k]
                else:
                    val -= cakes[j][k]
            tmp.append(val)
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)
