def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # a[i] = (a[0] + a[1] + ... + a[i]) % m
    for i in range(1, n):
        a[i] += a[i - 1]
    a = [a[i] % m for i in range(n)]
    a.sort()
    a.append(-1)
    ans = 0
    cnt = 1
    for i in range(n):
        if a[i] == a[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    print(ans)
