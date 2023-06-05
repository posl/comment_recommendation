def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]
    for i in range(N):
        B.append(B[i] + A[i])
    ans = float("inf")
    j = 1
    for i in range(2, N - 1):
        while B[i] - B[j] >= B[j]:
            j += 1
        ans = min(ans, max(B[j], B[i] - B[j]) - min(B[j], B[i] - B[j]))
        ans = min(ans, max(B[N] - B[i], B[i] - B[j]) - min(B[N] - B[i], B[i] - B[j]))
    print(ans)

if __name__ == '__main__':
    main()