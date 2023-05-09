def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    def check(i, j):
        for k in range(N):
            for l in range(N):
                if S[k][l] == '#':
                    if T[(k + i) % N][(l + j) % N] != '#':
                        return False
        return True
    for i in range(N):
        for j in range(N):
            if check(i, j):
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    solve()