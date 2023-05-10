def main():
    s = input()
    t = input()
    t_len = len(t)
    for i in range(t_len):
        if s[i] != t[i]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()