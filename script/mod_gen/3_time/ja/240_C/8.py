def main():
    N, X = map(int, input().split())
    sum = 0
    for i in range(N):
        a, b = map(int, input().split())
        sum += a
        if X < sum:
            print('No')
            exit()
        sum += b
        if X < sum:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()