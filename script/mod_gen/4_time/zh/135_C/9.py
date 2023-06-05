def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if A[i] >= B[i]:
            cnt += B[i]
            A[i] -= B[i]
            B[i] = 0
        else:
            cnt += A[i]
            B[i] -= A[i]
            A[i] = 0
            if A[i+1] >= B[i]:
                cnt += B[i]
                A[i+1] -= B[i]
                B[i] = 0
            else:
                cnt += A[i+1]
                B[i] -= A[i+1]
                A[i+1] = 0
    print(cnt)

if __name__ == '__main__':
    main()