def solve(n, d, walls):
    walls.sort()
    walls.append([10**9, 10**9])
    ans = 0
    cur = 0
    for i in range(n):
        while walls[cur][1] < walls[i][0]:
            cur += 1
        ans = max(ans, (walls[cur][0] - walls[i][0] + d - 1) // d + 1)
    return ans
