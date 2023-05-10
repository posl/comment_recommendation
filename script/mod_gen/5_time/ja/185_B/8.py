def main():
    # input
    N, M, T = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(M)]
    # compute
    battery = N
    time = 0
    for i in range(M):
        battery -= ABs[i][0] - time
        if battery <= 0:
            print('No')
            exit()
        battery += ABs[i][1] - ABs[i][0]
        battery = min(battery, N)
        time = ABs[i][1]
    battery -= T - time
    if battery <= 0:
        print('No')
        exit()
    # output
    print('Yes')

if __name__ == '__main__':
    main()