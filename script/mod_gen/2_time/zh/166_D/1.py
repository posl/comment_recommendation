def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    road = [list(map(int, input().split())) for _ in range(M)]
    good = [1] * N
    for i in range(M):
        if H[road[i][0]-1] <= H[road[i][1]-1]:
            good[road[i][0]-1] = 0
        if H[road[i][0]-1] >= H[road[i][1]-1]:
            good[road[i][1]-1] = 0
    print(sum(good))

if __name__ == '__main__':
    main()