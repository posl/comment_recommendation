def main():
    N, X = map(int, input().split())
    coin = []
    for i in range(N):
        A, B = map(int, input().split())
        coin.append([A, B])
    coin.sort(key=lambda x: x[0])
    count = 0
    for i in range(N):
        count += coin[i][0] * coin[i][1]
        if count > X:
            print('No')
            exit()
    if count >= X:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()