def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * (2 * 10 ** 5 + 1)
    for i in range(n):
        c[a[i]] += 1
    ans = 0
    for i in range(n):
        c[a[i]] -= 1
        for j in range(i + 1, n):
            c[a[j]] -= 1
            if c[a[i]] > 0:
                ans += c[a[i]]
            if c[a[j]] > 0:
                ans += c[a[j]]
            c[a[j]] += 1
    print(ans)
