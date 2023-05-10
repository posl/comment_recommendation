def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    s_index = 0
    t_index = 0
    while s_index < s_len and t_index < t_len:
        if s[s_index] == t[t_index]:
            s_index += 1
            t_index += 1
        else:
            t_index += 1
    if s_index == s_len:
        print('Yes')
    else:
        print('No')
