def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dot = 0
    for i in range(n):
        dot += a[i]*b[i]
    print('Yes' if dot == 0 else 'No')
solve()
