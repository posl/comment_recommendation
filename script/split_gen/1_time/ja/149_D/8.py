def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    score = 0
    for i in range(N):
        if i >= K and T[i] == T[i-K]:
            T = T[:i] + 'x' + T[i+1:]
        else:
            if T[i] == 'r':
                score += P
            elif T[i] == 's':
                score += R
            elif T[i] == 'p':
                score += S
    print(score)
