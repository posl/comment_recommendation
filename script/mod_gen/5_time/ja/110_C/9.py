def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s_dict.get(s[i]) == None:
            s_dict[s[i]] = t[i]
        elif s_dict[s[i]] != t[i]:
            print("No")
            return
        if t_dict.get(t[i]) == None:
            t_dict[t[i]] = s[i]
        elif t_dict[t[i]] != s[i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()