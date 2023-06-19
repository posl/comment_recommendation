def reverse(s, l, r):
    s = list(s)
    for i in range((r-l+1)//2):
        s[l+i-1], s[r-i-1] = s[r-i-1], s[l+i-1]
    return ''.join(s)

if __name__ == '__main__':
    reverse()