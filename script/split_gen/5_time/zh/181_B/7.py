def solve():
    N = int(input())
    sum = 0
    for i in range(N):
        a, b = map(int, input().split())
        sum += (b - a + 1) * (a + b) // 2
    print(sum)
solve()
