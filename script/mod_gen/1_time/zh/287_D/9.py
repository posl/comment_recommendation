def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(t_len+1):
        s_new = s[:i] + t_len * '?' + s[i+t_len:]
        #print(s_new)
        if s_new == t:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()