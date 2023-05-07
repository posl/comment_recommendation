def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * 200
    for i in range(N):
        cnt[A[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)
