def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = sum(A) // (N - 1)
    for i in range(1, N):
        ans[i] = A[i - 1] - ans[0]
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()