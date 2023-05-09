def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    # compute
    ans = 0
    for i in range(N):
        for j in range(i, N):
            x = min(A[i:j+1])
            ans = max(ans, (j-i+1)*x)
    # output
    print(ans)
