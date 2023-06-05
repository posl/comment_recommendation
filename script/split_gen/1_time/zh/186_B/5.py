def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_num = min([min(a) for a in A])
    ans = 0
    for a in A:
        for i in a:
            ans += i - min_num
    print(ans)
