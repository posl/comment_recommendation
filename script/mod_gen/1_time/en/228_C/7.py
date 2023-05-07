def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    C = [sum(p) for p in P]
    C.sort(reverse=True)
    print('Yes' if C[K-1] == C[K] else 'No')

if __name__ == '__main__':
    main()