def get_max_non_negative_integer(s):
    l = 0
    for i in range(1, len(s)):
        while i + l < len(s) and s[l] != s[i + l]:
            l += 1
        print(l)
        l = 0
