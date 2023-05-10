def main():
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    A = [AB[i][0] for i in range(M)]
    B = [AB[i][1] for i in range(M)]
    battery = N
    for i in range(M):
        battery -= A[i]
        if battery <= 0:
            print('No')
            exit()
        battery += B[i] - A[i]
        if battery > N:
            battery = N
    battery -= T - B[M - 1]
    if battery <= 0:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()