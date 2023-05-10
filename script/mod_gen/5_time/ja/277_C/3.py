def solve():
    N = int(input())
    AB = [ tuple(map(int, input().split())) for _ in range(N) ]
    AB.sort(key=lambda x: x[1])
    ans = 0
    for a, b in AB:
        if a > ans:
            ans = b
    print(ans)
solve()

if __name__ == '__main__':
    solve()