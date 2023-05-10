def main():
    s = input()
    t = input()
    t_len = len(t)
    s_len = len(s)
    for x in range(0, t_len + 1):
        if s[0:x] + s[s_len - t_len + x:s_len] == t:
            print('Yes')
        else:
            print('No')
