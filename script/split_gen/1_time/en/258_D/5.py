def solve():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    for a, b in AB:
        ans += a * b
        if ans > X:
            print(ans)
            return
    print(ans)
