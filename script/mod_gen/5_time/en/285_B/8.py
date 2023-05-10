def max_non_repeat_len(s):
    """Return the maximum non-negative integer l that satisfies all of the following conditions:
    l+i ≦ N, and
    for all integers k such that 1 ≦ k ≦ l, it holds that S_{k} ≠ S_{k+i}.
    Note that l=0 always satisfies the conditions.
    """
    n = len(s)
    max_l = 0
    for i in range(1, n):
        l = 0
        while (l+i < n) and (s[l] != s[l+i]):
            l += 1
        if l > max_l:
            max_l = l
    return max_l

if __name__ == '__main__':
    max_non_repeat_len()