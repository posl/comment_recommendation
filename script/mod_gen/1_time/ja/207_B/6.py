def solve():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
        return
    ans = 0
    while True:
        if A <= C * ans:
            print(ans)
            return
        A += B
        ans += 1

if __name__ == '__main__':
    solve()