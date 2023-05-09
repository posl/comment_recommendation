def is_contiguous_substring(s, t):
    if s == t:
        return True
    elif len(s) == 1:
        return False
    else:
        if s[0] == t[0]:
            return is_contiguous_substring(s[1:], t[1:])
        elif s[-1] == t[0]:
            return is_contiguous_substring(s[:-1], t[1:])
        else:
            return False

if __name__ == '__main__':
    is_contiguous_substring()