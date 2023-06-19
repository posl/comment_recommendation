def solve():
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    a.sort()
    ans = []
    for i in range(N):
        if i == 0:
            ans.append(a[i])
        else:
            if ans[-1][1] >= a[i][0]:
                ans[-1][1] = max(ans[-1][1], a[i][1])
            else:
                ans.append(a[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
solve()
