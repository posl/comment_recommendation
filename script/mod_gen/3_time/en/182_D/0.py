def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    B = [0] + B
    B.sort()
    ans = 0
    for i in range(N + 1):
        ans = max(ans, B[i + 1] - B[i])
    print(ans)

if __name__ == '__main__':
    main()