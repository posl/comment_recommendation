def main():
    n, k = map(int, input().split())
    S = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        if bin(i).count('1') != k:
            continue
        cnt = set()
        for j in range(n):
            if i >> j & 1:
                for c in S[j]:
                    cnt.add(c)
        if len(cnt) == k:
            ans = max(ans, bin(i).count('1'))
    print(ans)
