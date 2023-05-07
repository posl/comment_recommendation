def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * (N + 1)
    for i in range(N):
        count[A[i]] += 1
    ans = [0] * N
    for i in range(N):
        ans[i] = N - 1 - count[A[i]]
    for i in range(N):
        print(ans[i])
