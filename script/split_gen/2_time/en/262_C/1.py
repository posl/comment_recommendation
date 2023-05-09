def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    cnt = [0] * n
    for i in range(n):
        cnt[a[i] - 1] += 1
    ans = 0
    for i in range(n):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)
