def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0 for _ in range(10 ** 9 + 1)]
    for i in range(n):
        c[a[i]] += 1
    ans = 0
    for i in range(10 ** 9 + 1):
        ans += c[i] * (c[i] - 1) // 2
    print(ans)
