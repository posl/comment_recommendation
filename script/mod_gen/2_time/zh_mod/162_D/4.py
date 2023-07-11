def check(s, i, j, k):
    if s[i] == s[j] or s[i] == s[k] or s[j] == s[k]:
        return False
    if j - i == k - j:
        return False
    return True

if __name__ == '__main__':
    check()