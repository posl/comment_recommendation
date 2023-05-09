def max_non_negative_integer(s):
    N = len(s)
    max_non_negative_integer = [0] * (N-1)
    for i in range(0, N-1):
        j = 0
        while (i+j+1 < N) and (s[j] != s[i+j+1]):
            j += 1
        max_non_negative_integer[i] = j
    return max_non_negative_integer

if __name__ == '__main__':
    max_non_negative_integer()