def solve():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        ans += ab[i][0] / ab[i][1]
    ans /= 2
    ans2 = 0
    for i in range(n):
        ans2 += ab[i][0]
        if ans2 >= ans:
            ans2 -= ab[i][0]
            ans2 += (ans - ans2) * ab[i][1]
            break
    print(ans2)
solve()
