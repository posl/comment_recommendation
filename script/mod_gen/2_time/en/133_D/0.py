def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = (A[0] + A[N-1] - A[1]) // 2
    for i in range(1, N):
        ans[i] = A[i-1] - ans[i-1]
    print(" ".join(map(str, ans)))
main()

if __name__ == '__main__':
    main()