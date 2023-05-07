def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        m = 10**5
        for j in range(i, N):
            m = min(m, A[j])
            ans = max(ans, m * (j - i + 1))
    print(ans)
