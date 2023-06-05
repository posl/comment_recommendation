def is_equal(s, t):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i][j] != t[i][j]:
                return False
    return True

if __name__ == '__main__':
    is_equal()