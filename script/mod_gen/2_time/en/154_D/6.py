def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    E = [0] * (N - K + 1)
    for i in range(N - K + 1):
        E[i] = (p[i] + 1) / 2
        for j in range(1, K):
            E[i] += (p[i + j] + 1) / 2
    print(max(E))
main()

if __name__ == '__main__':
    main()