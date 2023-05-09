def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        if i % 2 != 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()