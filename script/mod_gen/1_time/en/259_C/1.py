def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print("No")
        return
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(t):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()