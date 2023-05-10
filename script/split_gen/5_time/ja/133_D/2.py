def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0]*N
    ans[0] = sum(A) - sum(A[1::2])*2
    for i in range(1, N):
        ans[i] = A[i-1]*2 - ans[i-1]
    print(*ans)
