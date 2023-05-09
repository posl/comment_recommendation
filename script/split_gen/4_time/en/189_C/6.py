def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        max_a = 0
        for j in range(i, N):
            max_a = max(max_a, A[j])
            ans = max(ans, max_a * (j - i + 1))
    print(ans)
