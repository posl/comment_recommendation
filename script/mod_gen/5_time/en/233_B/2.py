def reverseString(s, start, end):
    s = list(s)
    while(start < end):
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return ''.join(s)

if __name__ == '__main__':
    reverseString()