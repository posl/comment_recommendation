def solve():
    N, Q = map(int, input().split())
    S = input()
    AC = [0] * N
    for i in range(N - 1):
        if S[i] == 'A' and S[i + 1] == 'C':
            AC[i] = 1
    for i in range(N - 2, -1, -1):
        AC[i] += AC[i + 1]
    for i in range(Q):
        l, r = map(int, input().split())
        print(AC[l - 1] - AC[r - 1])

if __name__ == '__main__':
    solve()