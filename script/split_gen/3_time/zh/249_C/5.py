def main():
    n, k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    ans = 0
    for i in range(1 << n):
        cnt = 0
        for j in range(n):
            if i >> j & 1:
                cnt += 1
        if cnt != k:
            continue
        tmp = set()
        for j in range(n):
            if i >> j & 1:
                for c in s[j]:
                    tmp.add(c)
        if len(tmp) == k:
            ans = max(ans, cnt)
    print(ans)
