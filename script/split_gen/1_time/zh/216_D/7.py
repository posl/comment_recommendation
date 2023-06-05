def solve():
    N, M = map(int, input().split())
    k = [int(input()) for _ in range(M)]
    a = [list(map(int, input().split())) for _ in range(M)]
    print('Yes' if check(N, M, k, a) else 'No')
