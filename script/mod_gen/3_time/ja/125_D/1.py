def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if A[i-1] > 0:
            ans += A[i-1]
            A[i] += A[i-1]
            A[i-1] = 0
    if A[-1] > 0:
        ans += A[-1]
    print(ans)

if __name__ == '__main__':
    main()