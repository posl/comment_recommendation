def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        cnt = 0
        alp = [0] * 26
        for j in range(n):
            if i >> j & 1:
                cnt += 1
                for c in s[j]:
                    alp[ord(c) - 97] += 1
        if cnt != k:
            continue
        tmp = 0
        for j in range(26):
            if alp[j] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)
