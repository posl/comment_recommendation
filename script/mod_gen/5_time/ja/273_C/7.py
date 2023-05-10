def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * N
    C = [0] * N
    for i in range(N):
        if i == 0:
            B[i] = 1
        else:
            if A[i] != A[i-1]:
                B[i] = 1
    for i in range(N):
        if i == 0:
            C[i] = 1
        else:
            if A[N-i] != A[N-i-1]:
                C[i] = 1
    for i in range(N):
        if i != 0:
            B[i] = B[i] + B[i-1]
            C[i] = C[i] + C[i-1]
    for i in range(N):
        if i == 0:
            print(B[N-1])
        else:
            print(B[N-1]-B[i-1]-C[N-i-1])
main()

if __name__ == '__main__':
    main()