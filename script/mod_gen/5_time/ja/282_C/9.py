def solve():
    n = int(input())
    s = input()
    cnt = 0
    ans = ""
    for i in range(n):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',':
            if cnt % 2 == 1:
                ans += s[i]
            else:
                ans += '.'
        else:
            ans += s[i]
    print(ans)

if __name__ == '__main__':
    solve()