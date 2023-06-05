def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        if A[i] > B[i]:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        else:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        if A[i+1] > B[i]:
            ans += B[i]
            A[i+1] -= B[i]
            B[i] = 0
        else:
            ans += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
    print(ans)

if __name__ == '__main__':
    main()