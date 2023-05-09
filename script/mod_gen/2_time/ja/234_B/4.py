def main():
    N = int(input())
    P = []
    for i in range(N):
        x,y = map(int,input().split())
        P.append((x,y))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,(P[i][0]-P[j][0])**2+(P[i][1]-P[j][1])**2)
    print(ans**0.5)

if __name__ == '__main__':
    main()