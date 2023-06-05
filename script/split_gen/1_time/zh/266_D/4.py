def main():
    n = int(input())
    txa = [list(map(int, input().split())) for _ in range(n)]
    txa.insert(0, [0, 0, 0])
    ans = 0
    for i in range(1, n + 1):
        t, x, a = txa[i]
        ans += a
        if i == n:
            break
        dt = txa[i + 1][0] - t
        dx = abs(txa[i + 1][1] - x)
        if dt < dx or (dt - dx) % 2 != 0:
            print('No')
            exit()
    print('Yes')
    print(ans)
