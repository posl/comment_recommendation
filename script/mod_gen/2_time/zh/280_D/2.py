def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(t_len):
        if s[i] != t[i]:
            print(i+1)
            break
        if i == t_len-1:
            print(t_len)

if __name__ == '__main__':
    main()