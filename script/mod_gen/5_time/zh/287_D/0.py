def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(s_len - t_len + 1):
        s1 = s[:i] + s[i + t_len:]
        if t == s1.replace('?', 'a'):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()