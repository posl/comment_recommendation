def main():
    N = int(input())
    P = []
    for i in range(N):
        x,y = map(int,input().split())
        P.append([x,y])
    P.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (P[k][1] - P[i][1])*(P[j][0] - P[i][0]) == (P[j][1] - P[i][1])*(P[k][0] - P[i][0]):
                    ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()