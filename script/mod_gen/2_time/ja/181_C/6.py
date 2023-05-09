def main():
    N = int(input())
    P = []
    for _ in range(N):
        x,y = map(int,input().split())
        P.append([x,y])
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                x1,y1 = P[i]
                x2,y2 = P[j]
                x3,y3 = P[k]
                if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1):
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()