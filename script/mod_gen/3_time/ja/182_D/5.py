def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    if A[0] > 0:
        ans += A[0]
    for i in range(N-1):
        if A[i+1] > 0:
            if A[i] < 0:
                ans += A[i+1]
            else:
                ans += A[i+1] - A[i]
    print(ans)

if __name__ == '__main__':
    main()