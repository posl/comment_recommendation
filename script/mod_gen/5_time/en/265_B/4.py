def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(M):
        X, Y = map(int, input().split())
        A[X-1] = Y
    time = T
    for i in range(N-1):
        time = time - A[i]
        if time <= 0:
            print('No')
            exit()
        time = min(time+A[i+1]-A[i], T)
    time = time - A[N-1]
    if time <= 0:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()