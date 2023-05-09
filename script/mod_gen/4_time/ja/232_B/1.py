def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        print("No")
        return
    for i in range(s_len):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()