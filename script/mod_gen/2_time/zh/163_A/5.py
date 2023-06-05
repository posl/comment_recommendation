def calc(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                continue
            k = 2*j - i
            if k >= n:
                continue
            if s[i] == s[k] or s[j] == s[k]:
                continue
            cnt += 1
    return cnt

if __name__ == '__main__':
    calc()