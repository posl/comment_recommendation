def main():
    n = int(input())
    txa = [list(map(int, input().split())) for _ in range(n)]
    txa = [[0, 0, 0]] + txa + [[10**5 + 1, 0, 0]]
    ans = 0
    for i in range(n + 1):
        dt = txa[i + 1][0] - txa[i][0]
        dx = abs(txa[i + 1][1] - txa[i][1])
        if dt < dx:
            print(0)
            return
        elif (dt - dx) % 2 == 0:
            ans += txa[i][2]
    print(ans)
