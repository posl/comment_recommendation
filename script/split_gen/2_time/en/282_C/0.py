def main():
    n = int(input())
    s = input()
    ans = ""
    cnt = 0
    for i in range(n):
        if s[i] == '"':
            cnt += 1
            if cnt % 2 == 1:
                ans += '"'
            else:
                ans += '.'
        else:
            ans += s[i]
    print(ans)
