def reverseString(s, l, r):
    l -= 1
    r -= 1
    temp = s[l:r+1]
    temp = temp[::-1]
    s = s[:l] + temp + s[r+1:]
    return s
