def solve():
    #import sys
    #input = sys.stdin.readline
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    E = [list(map(int, input().split())) for _ in range(M)]
    E.sort()
    for i in range(M):
        if E[i][0] != i + 1:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    solve()