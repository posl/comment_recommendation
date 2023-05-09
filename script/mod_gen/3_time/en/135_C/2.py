def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] <= B[i]:
            count += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                count += A[i+1]
                A[i+1] = 0
            else:
                count += B[i]
                A[i+1] -= B[i]
        else:
            count += B[i]
    count += A[N]
    print(count)

if __name__ == '__main__':
    main()