def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0] * (N+1)
    for a in A:
        B[a] += 1
    ans = [0] * N
    for i in range(N):
        ans[i] = B[A[i]] - 1
    for a in ans:
        print(a)
