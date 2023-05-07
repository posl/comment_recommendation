def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print('No')
        return
    s = list(s)
    t = list(t)
    s_len = len(s)
    t_len = len(t)
    s_idx = 0
    t_idx = 0
    while t_idx < t_len:
        if s_idx >= s_len:
            print('No')
            return
        if s[s_idx] == t[t_idx]:
            s_idx += 1
            t_idx += 1
        else:
            s_idx += 1
    print('Yes')

if __name__ == '__main__':
    main()