def main():
    s = input()
    t = input()
    t_len = len(t)
    s_len = len(s)
    if t_len == 1:
        for i in range(s_len):
            if s[i] == '?':
                s = s[:i] + t + s[i+1:]
        if s == t:
            print('Yes')
        else:
            print('No')
    else:
        for i in range(s_len-t_len+1):
            if s[i] == '?':
                s = s[:i] + t + s[i+t_len:]
            elif s[i] != t[0]:
                continue
            else:
                if s[i:i+t_len] == t:
                    print('Yes')
                else:
                    print('No')
        if s[i+t_len] == '?':
            s = s[:i+t_len] + t + s[i+t_len+1:]
        elif s[i+t_len] != t[0]:
            pass
        else:
            if s[i+t_len:i+2*t_len] == t:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()