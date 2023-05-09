def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        if i % 2 == 0:
            ans[0] += A[i]
        else:
            ans[0] -= A[i]
    for i in range(1, N):
        ans[i] = (A[i - 1] - ans[i - 1] // 2) * 2
    print(*ans)
