def solve():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = []
    i = 0
    while i < N:
        l, r = LR[i]
        while i < N - 1 and r >= LR[i + 1][0]:
            r = max(r, LR[i + 1][1])
            i += 1
        ans.append([l, r])
        i += 1
    print(len(ans))
    for l, r in ans:
        print(l, r)
    return

if __name__ == '__main__':
    solve()