def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
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
                T = T[:i] + 'x' + T[i+1:]
            else:
                if T[i] == 'r':
                    ans += P
                elif T[i] == 's':
                    ans += R
                else:
                    ans += S
    print(ans)
