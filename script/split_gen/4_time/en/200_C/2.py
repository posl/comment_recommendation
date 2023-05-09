def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 200
    for i in range(N):
        B[A[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += B[i] * (B[i] - 1) // 2
    print(ans)
