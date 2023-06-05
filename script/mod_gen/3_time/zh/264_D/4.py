def solve(s):
    ans = 0
    for i in range(len(s)):
        if s[i] == 'a':
            continue
        if s[i] < 'a':
            ans += ord('z') - ord(s[i]) + 1
        else:
            ans += ord(s[i]) - ord('a')
        ans += 1
        ans += min(ord('z') - ord(s[i]), ord(s[i]) - ord('a'))
    return ans
s = input()
print(solve(s))
