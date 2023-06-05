def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(s_len - t_len + 1):
        flag = True
        for j in range(t_len):
            if s[i + j] != t[j] and s[i + j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()