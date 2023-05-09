def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P = sorted(P, key=lambda x: sum(x), reverse=True)
    print('Yes' if P[K-1][0] + P[K-1][1] + P[K-1][2] >= P[K][0] + P[K][1] + P[K][2] else 'No')

if __name__ == '__main__':
    main()