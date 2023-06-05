def solve():
    N, X = map(int, input().split())
    for i in range(N):
        A, B = map(int, input().split())
        X -= A * B
    if X >= 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()