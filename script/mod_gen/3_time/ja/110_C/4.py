def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        print("No")
        return
    s_dict = {}
    t_dict = {}
    for i in range(s_len):
        s_char = s[i]
        t_char = t[i]
        if s_char in s_dict:
            if s_dict[s_char] != t_char:
                print("No")
                return
        else:
            s_dict[s_char] = t_char
        if t_char in t_dict:
            if t_dict[t_char] != s_char:
                print("No")
                return
        else:
            t_dict[t_char] = s_char
    print("Yes")

if __name__ == '__main__':
    main()