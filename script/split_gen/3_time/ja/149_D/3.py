def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i >= K and T[i] == T[i-K]:
            T = T[:i] + 'x' + T[i+1:]
    for i in range(N):
        if T[i] == 'r':
            ans += P
        elif T[i] == 's':
            ans += R
        elif T[i] == 'p':
            ans += S
    print(ans)
