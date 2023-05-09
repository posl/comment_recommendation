def is_equal(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

if __name__ == '__main__':
    is_equal()