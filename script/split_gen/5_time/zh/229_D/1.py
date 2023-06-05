def main():
    s = input()
    k = int(input())
    ans = 0
    cnt = 0
    for c in s:
        if c == 'X':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    ans += k * 2
    ans = min(ans, len(s))
    print(ans)
