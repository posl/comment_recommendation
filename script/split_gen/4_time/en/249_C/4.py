def main():
    n, k = map(int, input().split())
    s = [list(input()) for _ in range(n)]
    ans = 0
    for i in range(26):
        cnt = 0
        for j in range(26):
            if i == j:
                continue
            for l in range(n):
                if chr(j+97) in s[l]:
                    cnt += 1
        if cnt >= n - k:
            ans += 1
    print(ans)
