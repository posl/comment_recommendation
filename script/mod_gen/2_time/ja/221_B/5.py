def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            s_list = list(s)
            s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
            s = "".join(s_list)
            break
    if s == t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()