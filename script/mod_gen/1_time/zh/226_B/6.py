def solve():
    n = int(input())
    d = {}
    for _ in range(n):
        l = int(input())
        a = tuple(map(int, input().split()))
        if a not in d:
            d[a] = 0
        d[a] += 1
    print(len(d))

if __name__ == '__main__':
    solve()