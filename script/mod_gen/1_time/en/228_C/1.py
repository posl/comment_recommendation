def main():
    N, K = map(int, input().split())
    P = []
    for _ in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: x[0] + x[1] + x[2] + x[3], reverse=True)
    print("Yes" if P[K-1][0] + P[K-1][1] + P[K-1][2] + P[K-1][3] >= P[K][0] + P[K][1] + P[K][2] + P[K][3] else "No")

if __name__ == '__main__':
    main()