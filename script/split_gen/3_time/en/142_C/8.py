def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = [0] * (N+1)
    for i in range(N, 0, -1):
        ans[i] = A[i]
        for j in range(2*i, N+1, i):
            ans[i] -= ans[j]
    print(*ans[1:])
