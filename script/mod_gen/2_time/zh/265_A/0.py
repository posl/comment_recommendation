def func(s):
    a = 'atcoder'
    ans = 0
    for i in range(len(s)):
        if s[i] == a[i]:
            continue
        else:
            index = s[i:].find(a[i])
            if index == -1:
                ans += len(s) - i
                break
            else:
                ans += index
                s = s[:i] + s[i+index] + s[i:i+index] + s[i+index+1:]
    return ans
s = input()
print(func(s))
