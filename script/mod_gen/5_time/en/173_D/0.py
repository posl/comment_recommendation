def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        ans += min(A[i], A[i+1])
    ans += A[0]
    ans += A[-1]
    print(ans)

if __name__ == '__main__':
    main()