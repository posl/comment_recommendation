def main():
    N, X = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    sum = 0
    for i in range(N):
        if i % 2 == 0:
            sum += b[i]
        else:
            sum += a[i]
    if sum >= X:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()