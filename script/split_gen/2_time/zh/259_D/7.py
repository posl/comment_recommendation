def solve():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len >= t_len:
        print('No')
        return
    if s == t[:s_len]:
        print('Yes')
    else:
        print('No')
