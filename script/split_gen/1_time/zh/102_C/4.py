def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(0, N):
        B[i] = A[i] - i - 1
    B.sort()
    b = B[N // 2]
    ans = 0
    for i in range(0, N):
        ans += abs(A[i] - (b + i + 1))
    print(ans)
main()
