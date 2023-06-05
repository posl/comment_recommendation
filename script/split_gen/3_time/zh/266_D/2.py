def main():
    n = int(input())
    txa = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        if i == 0:
            ans += txa[i][2]
        else:
            ans += txa[i][2]
            if txa[i][0] - txa[i - 1][0] >= abs(txa[i][1] - txa[i - 1][1]):
                if (txa[i][1] - txa[i - 1][1]) % 2 == 0:
                    ans -= (txa[i][1] - txa[i - 1][1]) // 2
                else:
                    ans -= (txa[i][1] - txa[i - 1][1]) // 2 + 1
            else:
                ans = 0
                break
    print(ans)
