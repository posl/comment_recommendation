def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    cnt = {}
    for i in range(n):
        if a[i] in cnt:
            cnt[a[i]] += 1
        else:
            cnt[a[i]] = 1
        ans[i] = len(cnt)
    for i in range(n):
        print(ans[i])
