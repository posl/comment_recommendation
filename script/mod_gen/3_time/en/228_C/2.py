def main():
    N, K = map(int, input().split())
    P = []
    for _ in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    for i in range(N):
        if P[i][0] + P[i][1] + P[i][2] + P[K - 1][0] + P[K - 1][1] + P[K - 1][2] >= 300 * K:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()