def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        if sum(P[i]) >= (K-1)*300:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()