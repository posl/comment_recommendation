def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N+1)]
    for a in A:
        B[a] += 1
    ans = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        ans[i] = (B[i] * (B[i] - 1)) // 2
    total = sum(ans)
    for a in A:
        print(total - ans[a] + (B[a] - 1) * (B[a] - 2) // 2)
