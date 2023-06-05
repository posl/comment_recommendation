def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    for i in range(len_s - len_t + 1):
        flag = True
        for j in range(len_t):
            if s[i+j] != t[j] and s[i+j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
    for i in range(len_t, len_s):
        print('No')

if __name__ == '__main__':
    main()