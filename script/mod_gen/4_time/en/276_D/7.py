def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if sum([i % 2 for i in a]) == 0:
            a = [i // 2 for i in a]
            ans += 1
        else:
            break
    while True:
        if sum([i % 3 for i in a]) == 0:
            a = [i // 3 for i in a]
            ans += 1
        else:
            break
    if sum([i % 3 for i in a]) == 0:
        print(ans)
    else:
        print(-1)
solve()
