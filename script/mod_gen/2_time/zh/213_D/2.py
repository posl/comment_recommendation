def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB.sort()
    ans = [1]
    for i in range(N-1):
        a, b = AB[i]
        if a == ans[-1]:
            ans.append(b)
        elif b == ans[-1]:
            ans.append(a)
    print(*ans)
solve()
