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
            for j in range(i, len(s)):
                if s[j] != t[j]:
                    if ord(s[j]) - ord('a') != (ord(t[j]) - ord('a') + k) % 26:
                        print("No")
                        return
            print("Yes")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()