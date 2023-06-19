def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    for i in range(len_t + 1):
        s1 = s[:i] + t[i:] #用t的后半部分替换s的前半部分
        s2 = s[len_s - len_t + i:] + s[:i] #用t的后半部分替换s的前半部分
        if (s1.replace('?', 'a') == t) or (s2.replace('?', 'a') == t):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()