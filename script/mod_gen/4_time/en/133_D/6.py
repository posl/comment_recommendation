def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0 for i in range(N)]
    ans[0] = (A[1] - A[N-1]) // 2
    for i in range(1, N):
        ans[i] = A[i-1] - ans[i-1]
    for i in range(N):
        print(ans[i], end=' ')
    print()

if __name__ == '__main__':
    main()