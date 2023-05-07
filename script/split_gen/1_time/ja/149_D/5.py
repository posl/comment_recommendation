def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = list(input())
    ans = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            else:
                ans += S
        else:
            if T[i] == T[i-K]:
                if i+K < N:
                    if T[i] == 'r' and T[i+K] != 'p':
                        T[i] = 'p'
                        ans += P
                    elif T[i] == 's' and T[i+K] != 'r':
                        T[i] = 'r'
                        ans += R
                    elif T[i] == 'p' and T[i+K] != 's':
                        T[i] = 's'
                        ans += S
                else:
                    if T[i] == 'r':
                        T[i] = 'p'
                        ans += P
                    elif T[i] == 's':
                        T[i] = 'r'
                        ans += R
                    elif T[i] == 'p':
                        T[i] = 's'
                        ans += S
            else:
                if T[i] == 'r':
                    ans += P
                elif T[i] == 's':
                    ans += R
                else:
                    ans += S
    print(ans)
