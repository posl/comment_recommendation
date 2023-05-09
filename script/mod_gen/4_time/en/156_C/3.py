def solve():
    N = int(input())
    X = list(map(int, input().split()))
    min_total = 10000000000
    for i in range(1, 101):
        total = 0
        for j in range(N):
            total += (X[j] - i) ** 2
        if total < min_total:
            min_total = total
    print(min_total)

if __name__ == '__main__':
    solve()