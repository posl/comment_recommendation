def main():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        A_, B_ = map(int, input().split())
        A.append(A_)
        B.append(B_)
    #print(N, M, T)
    #print(A)
    #print(B)
    battery = N
    for i in range(M):
        battery -= A[i] - T
        if battery <= 0:
            print('No')
            return
        battery += B[i] - A[i]
        if battery >= N:
            battery = N
        T = B[i]
    battery -= T
    if battery <= 0:
        print('No')
        return
    print('Yes')

if __name__ == '__main__':
    main()