def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(K):
        ans += R if T[i] == 's' else S if T[i] == 'p' else P if T[i] == 'r' else 0
        if i + K < N and T[i] == T[i + K]:
            T = T[:i + K] + 'x' + T[i + K + 1:]
    for i in range(K, N):
        ans += R if T[i] == 's' else S if T[i] == 'p' else P if T[i] == 'r' else 0
    print(ans)

if __name__ == '__main__':
    main()