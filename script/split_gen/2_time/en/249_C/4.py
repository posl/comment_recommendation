def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1, 2**n):
        tmp = set()
        for j in range(n):
            if i & (1 << j):
                tmp |= set(s[j])
        if len(tmp) == k:
            ans = max(ans, len(tmp))
    print(ans)
