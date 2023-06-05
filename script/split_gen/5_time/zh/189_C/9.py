def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for left in range(N):
        x = A[left]
        for right in range(left, N):
            x = min(x, A[right])
            ans = max(ans, x * (right - left + 1))
    print(ans)
