def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(M):
        X, Y = map(int, input().split())
        B.append((X, Y))
    B.append((N, 0))
    B.sort()
    time = T
    for i in range(M+1):
        time -= A[B[i][0]-2]
        if time <= 0:
            print('No')
            return
        time += B[i][1]
        if time > T:
            time = T
    print('Yes')
    return

if __name__ == '__main__':
    main()