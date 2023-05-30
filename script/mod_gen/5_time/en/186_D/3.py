def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += i * A[i] - (N - i) * A[i-1]
    print(ans)
main()
