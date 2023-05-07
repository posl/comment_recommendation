def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in range(N):
        ans.append(0)
    ans[0] = sum(A) - N * A[1]
    for i in range(1, N):
        ans[i] = 2 * A[i-1] - ans[i-1]
    for i in range(N):
        print(ans[i], end=" ")
    print()
