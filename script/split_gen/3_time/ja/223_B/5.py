def solve():
    s = input()
    s_min = s
    s_max = s
    for _ in range(len(s)):
        s = s[1:] + s[0]
        s_min = min(s_min, s)
        s_max = max(s_max, s)
    print(s_min)
    print(s_max)
