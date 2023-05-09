def main():
    # input
    N, M = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(M)]
    # compute
    ABs.sort(key=lambda x: x[0])
    ABs.sort(key=lambda x: x[1])
    # output
    for i in range(M-1):
        if ABs[i][1] == ABs[i+1][0]:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()