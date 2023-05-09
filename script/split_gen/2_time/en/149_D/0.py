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
            if T[i] == 'r' and T[i-K] != 'p':
                ans += P
                T = T[:i] + 'p' + T[i+1:]
            elif T[i] == 's' and T[i-K] != 'r':
                ans += R
                T = T[:i] + 'r' + T[i+1:]
            elif T[i] == 'p' and T[i-K] != 's':
                ans += S
                T = T[:i] + 's' + T[i+1:]
    print(ans)
