def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(s_len):
        if s[i:i+t_len] == t:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()