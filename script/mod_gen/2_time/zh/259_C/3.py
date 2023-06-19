def main():
    s = input()
    t = input()
    if len(s) + 1 != len(t):
        print("No")
        return
    i = 0
    j = 0
    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i += 1
        else:
            if i == j:
                j += 1
            else:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()