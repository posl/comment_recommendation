def main():
    n, k = map(int, input().split())
    s = [input() for i in range(n)]
    ans = 0
    for i in range(1 << n):
        cnt = 0
        tmp = set()
        for j in range(n):
            if i & (1 << j):
                cnt += 1
                for c in s[j]:
                    tmp.add(c)
        if cnt != k:
            continue
        if len(tmp) > ans:
            ans = len(tmp)
    print(ans)
