def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        P[i].sort()
    P.sort()
    for i in range(N):
        if sum(P[i]) >= sum(P[K-1]):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()