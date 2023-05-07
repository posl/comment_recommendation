def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        x = A[i]
        for j in range(i, N):
            x = min(x, A[j])
            ans = max(ans, x*(j-i+1))
    print(ans)
