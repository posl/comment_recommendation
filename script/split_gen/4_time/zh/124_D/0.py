def main():
    n, k = map(int, input().split())
    s = input()
    ans = 0
    cnt = 0
    for i in range(n):
        if s[i] == '0':
            cnt += 1
        else:
            if k > 0:
                k -= 1
                cnt += 1
            else:
                cnt -= 1
        ans = max(ans, cnt)
    print(ans)
