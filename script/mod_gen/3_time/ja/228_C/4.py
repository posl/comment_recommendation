def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    S = [sum(p) for p in P]
    rank = [0] * N
    for i in range(N):
        for j in range(N):
            if S[i] < S[j]:
                rank[i] += 1
    for i in range(N):
        if rank[i] <= K-1:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()