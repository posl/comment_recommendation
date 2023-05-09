def solve():
    N, M = map(int, input().split())
    for i in range(M):
        input()
    if M == N - 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()