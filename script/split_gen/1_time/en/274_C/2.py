def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2**N+1)
    for i in range(N):
        ans[A[i]] += 1
        ans[A[i]*2] += ans[A[i]]
        ans[A[i]*2+1] += ans[A[i]]
        ans[A[i]] = 0
    for i in range(1, 2**N+1):
        print(ans[i])
