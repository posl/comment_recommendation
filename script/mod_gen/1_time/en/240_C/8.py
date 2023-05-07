def main():
    N, X = map(int, input().split())
    sum = 0
    for i in range(N):
        a, b = map(int, input().split())
        sum += a * b
        if sum > X * 100:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()