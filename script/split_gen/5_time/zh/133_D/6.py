def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = A[i] - sum(ans) // 2
    print(*ans)
