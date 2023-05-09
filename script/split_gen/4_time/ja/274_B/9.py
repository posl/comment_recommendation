def solve():
    H, W = map(int, input().split())
    ans = []
    for i in range(H):
        ans.append(input().count("#"))
    print(*ans)
