def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = sum(A) - 2 * sum(A[1::2])
    for i in range(N-1):
        ans[i+1] = 2 * A[i] - ans[i]
    print(*ans)
