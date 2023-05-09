def check(s, t, n, m):
    for i in range(n - m + 1):
        for j in range(m):
            if s[i + j] != t[j]:
                break
        else:
            return True
    return False

if __name__ == '__main__':
    check()