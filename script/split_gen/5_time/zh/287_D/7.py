def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(t_len + 1):
        s_ = s[0:i] + t_len * '?' + s[i + t_len:]
        if s_ == t:
            print('Yes')
        else:
            print('No')
