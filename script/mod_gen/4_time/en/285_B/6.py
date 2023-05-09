def get_max_non_negative_integer(s):
    n = len(s)
    max_non_negative_integer = [0] * n
    for i in range(1, n):
        for l in range(1, n - i):
            if s[l] != s[l + i]:
                max_non_negative_integer[i] = l
    return max_non_negative_integer

if __name__ == '__main__':
    get_max_non_negative_integer()