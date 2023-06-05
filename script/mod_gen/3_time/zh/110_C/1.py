def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    dict1 = {}
    dict2 = {}
    for i in range(len(s)):
        if s[i] in dict1:
            if dict1[s[i]] != t[i]:
                print("No")
                return
        else:
            dict1[s[i]] = t[i]
        if t[i] in dict2:
            if dict2[t[i]] != s[i]:
                print("No")
                return
        else:
            dict2[t[i]] = s[i]
    print("Yes")

if __name__ == '__main__':
    main()