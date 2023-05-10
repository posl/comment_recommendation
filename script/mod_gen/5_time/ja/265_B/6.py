def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    time = T
    prev = 0
    for i in range(N-1):
        time -= A[i] - prev
        if time <= 0:
            print('No')
            return
        time += XY[i][1] - XY[i][0]
        if time > T:
            time = T
        prev = A[i]
    time -= A[N-1] - prev
    if time <= 0:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()