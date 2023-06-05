def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            for j in range(i+1,len(s)):
                if s[i] == t[j] and s[j] == t[i]:
                    s = s[:i] + t[i] + s[i+1:j] + t[j] + s[j+1:]
                    break
            else:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()