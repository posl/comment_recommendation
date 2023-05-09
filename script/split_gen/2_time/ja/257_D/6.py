def main():
    N = int(input())
    jump = []
    for i in range(N):
        x, y, p = map(int, input().split())
        jump.append((x, y, p))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            d = abs(jump[i][0] - jump[j][0]) + abs(jump[i][1] - jump[j][1])
            if jump[i][2]*ans < d:
                ans = d // jump[i][2] + 1
            if jump[j][2]*ans < d:
                ans = d // jump[j][2] + 1
    print(ans)
