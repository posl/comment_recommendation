def max_l(s, i):
    l = 0
    while i + l < len(s):
        if s[l] != s[i + l]:
            l += 1
        else:
            break
    return l

if __name__ == '__main__':
    max_l()