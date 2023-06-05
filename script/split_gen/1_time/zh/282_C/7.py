def solve():
    n = int(input())
    s = input()
    ans = ""
    for i in range(n):
        if i % 2 == 0:
            ans += s[i]
        else:
            if s[i] == '"':
                ans += '"'
            else:
                ans += '.'
    print(ans)
