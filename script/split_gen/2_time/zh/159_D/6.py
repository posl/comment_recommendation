def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * N
    for i in range(N):
        cnt[A[i] - 1] += 1
    ans = 0
    for i in range(N):
        ans += cnt[i] * (cnt[i] - 1) // 2
    for i in range(N):
        print(ans - (cnt[A[i] - 1] - 1))
