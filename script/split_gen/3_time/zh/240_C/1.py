def solve():
    N, X = map(int, input().split())
    for i in range(N):
        a, b = map(int, input().split())
        if X == a or X == b or X == a + b:
            print('Yes')
            return
    print('No')
solve()
