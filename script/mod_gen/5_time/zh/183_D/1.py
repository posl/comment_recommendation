def main():
    N, W = map(int, input().split())
    stp = [list(map(int, input().split())) for _ in range(N)]
    stp.sort(key=lambda x: x[0])
    stp.sort(key=lambda x: x[1])
    # print(stp)
    water = 0
    for stpi in stp:
        water += stpi[2]
        if water > W:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()