def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    num = 0
    for i in range(N):
        if B[i] >= A[i]:
            num += A[i]
            B[i] = B[i] - A[i]
            if B[i] >= A[i+1]:
                num += A[i+1]
                A[i+1] = 0
            else:
                num += B[i]
                A[i+1] = A[i+1] - B[i]
        else:
            num += B[i]
    print(num)

if __name__ == '__main__':
    main()