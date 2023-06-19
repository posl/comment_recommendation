def get_next_permutation(s):
    n = len(s)
    for i in range(n-1, 0, -1):
        if s[i-1] < s[i]:
            break
    if i == 1 and s[0] >= s[1]:
        return None
    for j in range(n-1, i-1, -1):
        if s[j] > s[i-1]:
            break
    s[i-1], s[j] = s[j], s[i-1]
    s[i:] = s[i:][::-1]
    return s
