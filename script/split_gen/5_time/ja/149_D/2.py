def main():
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
            else:
                score += S
        else:
            if T[i] == 'r':
                if T[i-K] == 'r':
                    T[i] = 'x'
                else:
                    score += P
            elif T[i] == 's':
                if T[i-K] == 's':
                    T[i] = 'x'
                else:
                    score += R
            else:
                if T[i-K] == 'p':
                    T[i] = 'x'
                else:
                    score += S
    print(score)
