def solve():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == "v":
            ans += 1
    print(ans)
