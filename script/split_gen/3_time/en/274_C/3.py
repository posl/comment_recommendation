def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = [0] * (2 * N + 1)
    for i in range(1, N + 1):
        ans[A[i]] = ans[A[i] // 2] + 1
    for i in range(1, 2 * N + 1):
        print(ans[i])
