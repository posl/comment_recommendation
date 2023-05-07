def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0]+x[1]+x[2], reverse=True)
    #print(P)
    #print(P[K-1][0]+P[K-1][1]+P[K-1][2])
    for i in range(N):
        if P[i][0]+P[i][1]+P[i][2] >= P[K-1][0]+P[K-1][1]+P[K-1][2]:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()