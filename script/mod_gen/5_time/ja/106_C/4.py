def get_string(s, k):
    if k == 0:
        return s[0]
    i = 0
    while True:
        if i >= len(s):
            break
        n = int(s[i])
        if n != 1:
            if k <= len(s[i:]) * (n - 1):
                return s[i + (k - 1) // (n - 1)]
            k -= len(s[i:]) * (n - 1)
        i += 1
    return s[-1]

if __name__ == '__main__':
    get_string()