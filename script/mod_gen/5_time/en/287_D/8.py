def main():
    s = input()
    t = input()
    t_len = len(t)
    s_len = len(s)
    for i in range(t_len+1):
        if s[:i] + t_len - i + s[s_len - (t_len-i):] == t.replace('?', 'a'):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()