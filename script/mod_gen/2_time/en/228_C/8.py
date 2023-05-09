def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        P[i].sort()
        P[i].reverse()
        P[i] = P[i][0] + P[i][1] + P[i][2]
    P.sort()
    P.reverse()
    if P[K-1] >= sum(P[:K]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()