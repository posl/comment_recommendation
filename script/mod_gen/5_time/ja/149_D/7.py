def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    score = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                score += P
            elif T[i] == 's':
                score += R
            elif T[i] == 'p':
                score += S
        else:
            if T[i] == 'r' and T[i-K] != 'r':
                score += P
            elif T[i] == 's' and T[i-K] != 's':
                score += R
            elif T[i] == 'p' and T[i-K] != 'p':
                score += S
    print(score)

if __name__ == '__main__':
    solve()