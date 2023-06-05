def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    mod = [0] * n
    mod[0] = a[0] % m
    for i in range(1, n):
        mod[i] = (mod[i - 1] + a[i]) % m
    mod.sort()
    ans = 0
    cnt = 1
    for i in range(1, n):
        if mod[i] == mod[i - 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)
