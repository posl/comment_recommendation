def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N - 1)
    for i in range(N - 1):
        B[i] = A[i + 1] - A[i]
    #print(B)
    ans = 0
    for i in range(N - M):
        ans += max(0, sum(B[i : i + M]))
    print(ans)

if __name__ == '__main__':
    main()