def main():
    #N: number of friends
    #K: minimum height to ride the roller coaster
    N, K = map(int, input().split())
    #h: height of each friend
    h = list(map(int, input().split()))
    #count: number of friends who can ride the roller coaster
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    print(count)

if __name__ == '__main__':
    main()