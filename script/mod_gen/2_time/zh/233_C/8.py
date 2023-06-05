def reverseString(s, l, r):
    s = s[:l-1] + s[l-1:r][::-1] + s[r:]
    return s

if __name__ == '__main__':
    reverseString()