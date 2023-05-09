def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        if i % 2 == 0:
            ans[0] += A[i]
        else:
            ans[0] -= A[i]
    for i in range(1, N):
        ans[i] = 2 * A[i-1] - ans[i-1]
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()