def check_if_exists(a, p, q, r):
    n = len(a)
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    for i in range(n):
        for j in range(i + 2, n):
            for k in range(j + 2, n):
                for l in range(k + 2, n + 1):
                    if s[j] - s[i] == p and s[k] - s[j] == q and s[l] - s[k] == r:
                        return True
    return False

if __name__ == '__main__':
    check_if_exists()