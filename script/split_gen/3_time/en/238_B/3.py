def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 360
    for i in range(N):
        ans = min(ans, abs(360 - 2 * (sum(A[i:]) % 360)))
    print(ans)
