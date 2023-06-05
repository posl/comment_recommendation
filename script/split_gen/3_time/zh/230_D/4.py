def main():
    N, D = map(int, input().split())
    wall = []
    for i in range(N):
        L, R = map(int, input().split())
        wall.append([L, R])
    wall.sort()
    ans = 0
    for i in range(N):
        L = wall[i][0]
        R = wall[i][1]
        if L != R:
            if R - L < D:
                ans += 1
            elif R - L == D:
                ans += 2
            else:
                ans += 2
                ans += (R - L - D) // D
    print(ans)
