def main():
    n, k = map(int, input().split())
    s = [set(input()) for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        if bin(i).count("1") != k:
            continue
        t = set()
        for j in range(n):
            if i >> j & 1:
                t |= s[j]
        ans = max(ans, len(t))
    print(ans)
