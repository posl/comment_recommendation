def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    rank = [1] * N
    for i in range(1, N):
        if P[i - 1][0] + P[i - 1][1] + P[i - 1][2] == P[i][0] + P[i][1] + P[i][2]:
            rank[i] = rank[i - 1]
        else:
            rank[i] = i + 1
    for i in range(N):
        if rank[i] <= K:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()