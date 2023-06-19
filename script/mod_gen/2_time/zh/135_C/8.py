def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= B[i]:
            ans += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                ans += A[i+1]
                B[i] -= A[i+1]
            else:
                ans += B[i]
        else:
            ans += B[i]
    print(ans)
    return

if __name__ == '__main__':
    main()