def solve():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    ans = 1
    for a, b in ab:
        if ans < a:
            ans = b
    print(ans)

if __name__ == '__main__':
    solve()