def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = sum(A) - (N - 2) * A[0]
    for i in range(1, N):
        ans[i] = 2 * A[i - 1] - ans[i - 1]
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()