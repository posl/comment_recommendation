def main():
    N,K,A = input().split()
    N = int(N)
    K = int(K)
    A = int(A)
    if N == 1:
        print(1)
        return
    else:
        if K % N == 0:
            if A == N:
                print(1)
                return
            else:
                print(A + K % N - 1)
                return
        else:
            if A + K % N - 1 <= N:
                print(A + K % N - 1)
                return
            else:
                print(A + K % N - 1 - N)
                return

if __name__ == '__main__':
    main()