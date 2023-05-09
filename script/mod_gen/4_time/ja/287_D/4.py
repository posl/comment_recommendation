def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    for i in range(len_s - len_t + 1):
        s_part = s[i:i+len_t]
        match = True
        for j in range(len_t):
            if s_part[j] != t[j] and s_part[j] != '?':
                match = False
                break
        if match:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()