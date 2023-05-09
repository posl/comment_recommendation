def main():
    N = int(input())
    jump = []
    for i in range(N):
        x, y, p = map(int, input().split())
        jump.append([x, y, p])
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            d = abs(jump[i][0] - jump[j][0]) + abs(jump[i][1] - jump[j][1])
            if jump[i][2] * ans >= d:
                continue
            else:
                ans = d / jump[i][2]
    print(int(ans + 1))
