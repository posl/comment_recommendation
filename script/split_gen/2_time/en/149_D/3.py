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
            elif T[i] == 'p':
                score += S
        else:
            if T[i] == T[i-K]:
                if i+K < N:
                    if T[i] == 'r' and T[i+K] == 'r':
                        T = T[:i]+'p'+T[i+1:]
                    elif T[i] == 's' and T[i+K] == 's':
                        T = T[:i]+'r'+T[i+1:]
                    elif T[i] == 'p' and T[i+K] == 'p':
                        T = T[:i]+'s'+T[i+1:]
                    else:
                        if T[i+K] == 'r':
                            T = T[:i]+'p'+T[i+1:]
                            score += P
                        elif T[i+K] == 's':
                            T = T[:i]+'r'+T[i+1:]
                            score += R
                        elif T[i+K] == 'p':
                            T = T[:i]+'s'+T[i+1:]
                            score += S
                else:
                    if T[i] == 'r':
                        T = T[:i]+'p'+T[i+1:]
                    elif T[i] == 's':
                        T = T[:i]+'r'+T[i+1:]
                    elif T[i] == 'p':
                        T = T[:i]+'s'+T[i+1:]
            else:
                if T[i] == 'r':
                    score += P
                elif T[i] == 's':
                    score += R
                elif T[i] == 'p':
                    score += S
    print(score)
