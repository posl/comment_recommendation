def get_id(s):
    base = ord('A')
    len_s = len(s)
    max_len = 0
    for i in range(len_s):
        max_len += (26 ** i)
    if len_s == 1:
        return ord(s) - base + 1
    else:
        ans = 0
        for i in range(len_s):
            if i == 0:
                ans += (ord(s[i]) - base) * (26 ** (len_s - i - 1))
            else:
                ans += (ord(s[i]) - base + 1) * (26 ** (len_s - i - 1))
        return ans + max_len
