def main():
    s = input()
    t = input()
    if len(s) + 1 != len(t):
        print("No")
        return
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(s):
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()