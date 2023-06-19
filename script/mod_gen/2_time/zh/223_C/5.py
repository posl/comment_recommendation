def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    left = 0
    right = 0
    for i in range(N):
        left += A[i] / B[i]
    for i in range(N - 1, -1, -1):
        right += A[i] / B[i]
    ans = 0
    for i in range(N):
        ans += A[i]
    ans -= left
    ans -= right
    print(ans)

if __name__ == '__main__':
    main()