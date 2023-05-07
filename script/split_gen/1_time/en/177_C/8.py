def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    ans = 0
    for i in range(1, N+1):
        ans += A[i] * (i * (N-i+1) + (N-i+1) * (N-i) // 2)
    print(ans % (10**9+7))
