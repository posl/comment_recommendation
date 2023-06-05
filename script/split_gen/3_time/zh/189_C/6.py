def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            x = min(A[i:j+1])
            ans = max(ans, (j-i+1)*x)
    print(ans)
