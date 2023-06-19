def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    path = [list(map(int,input().split())) for _ in range(M)]
    good = [True] * N
    for i in range(M):
        if H[path[i][0]-1] <= H[path[i][1]-1]:
            good[path[i][0]-1] = False
        if H[path[i][1]-1] <= H[path[i][0]-1]:
            good[path[i][1]-1] = False
    print(good.count(True))

if __name__ == '__main__':
    main()