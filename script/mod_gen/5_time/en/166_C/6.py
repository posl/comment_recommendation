def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    AB = [list(map(int,input().split())) for _ in range(M)]
    good = [True]*N
    for i in range(M):
        if H[AB[i][0]-1] >= H[AB[i][1]-1]:
            good[AB[i][1]-1] = False
        if H[AB[i][0]-1] <= H[AB[i][1]-1]:
            good[AB[i][0]-1] = False
    print(good.count(True))

if __name__ == '__main__':
    main()