def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = [0] * (N + 1)
    for i in range(N):
        C[P[i]] = i
    for i in range(K, N + 1):
        print(max(P[:i]) - min(P[C[max(P[:i])]:i + 1]) + 1)

if __name__ == '__main__':
    main()