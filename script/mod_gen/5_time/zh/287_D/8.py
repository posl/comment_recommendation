def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len < t_len:
        print("No")
        return
    for i in range(t_len):
        if s[i] == t[i] or s[i] == "?":
            continue
        else:
            print("No")
            return
    print("Yes")
    for i in range(t_len, s_len):
        if s[i] == "?":
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()