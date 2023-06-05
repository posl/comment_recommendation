def solve():
    N, D = map(int, input().split())
    walls = []
    for _ in range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort()
    ans = 0
    i = 0
    while i < N:
        L = walls[i][0]
        R = walls[i][1]
        if L + D <= R:
            ans += 1
            i += 1
            continue
        else:
            j = i + 1
            while j < N:
                L2 = walls[j][0]
                R2 = walls[j][1]
                if L2 + D <= R:
                    ans += 1
                    i = j + 1
                    break
                else:
                    j += 1
            else:
                ans += 1
                i += 1
    print(ans)
solve()
