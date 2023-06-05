def reverse(s, l, r):
    s = list(s)
    for i in range((r-l+1)//2):
        s[l+i], s[r-i] = s[r-i], s[l+i]
    return ''.join(s)

if __name__ == '__main__':
    reverse()