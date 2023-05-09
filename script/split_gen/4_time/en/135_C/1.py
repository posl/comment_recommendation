def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        A[i] -= min(A[i], B[i])
        B[i] -= min(A[i-1], B[i])
        ans += min(A[i], B[i])
    print(ans)
main()
I made a mistake in the problem statement. I'm sorry for the inconvenience.
