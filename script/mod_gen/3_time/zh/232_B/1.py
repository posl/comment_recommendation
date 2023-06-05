def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            k = ord(t[i]) - ord(s[i])
            if k < 0:
                k += 26
            for j in range(i+1, len(s)):
                if s[j] != t[j]:
                    if ord(t[j]) - ord(s[j]) != k:
                        print("No")
                        return
            print("Yes")
            return
    print("Yes")

if __name__ == '__main__':
    main()