def reverse_str(s, l, r):
    s = list(s)
    for i in range((r-l+1)//2):
        s[l-1+i], s[r-1-i] = s[r-1-i], s[l-1+i]
    return ''.join(s)

if __name__ == '__main__':
    reverse_str()