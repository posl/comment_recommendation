def solve():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(' '.join(map(str, Q)))

if __name__ == '__main__':
    solve()