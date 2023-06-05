def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    cnt = [0] * 200
    for i in range(n):
        ans += cnt[a[i] % 200]
        cnt[a[i] % 200] += 1
    print(ans)
