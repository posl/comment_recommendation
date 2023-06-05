def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)
