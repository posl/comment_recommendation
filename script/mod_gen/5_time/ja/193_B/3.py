def solve():
    n = int(input())
    min_cost = 10**9 + 1
    for _ in range(n):
        a, p, x = map(int, input().split())
        if x > a:
            min_cost = min(min_cost, p)
    if min_cost == 10**9 + 1:
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    solve()