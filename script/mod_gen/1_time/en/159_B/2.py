def main():
    s = input()
    n = len(s)
    if s == s[::-1]:
        if s[:n//2] == s[:n//2][::-1]:
            if s[n//2+1:] == s[n//2+1:][::-1]:
                print("Yes")
                return
    print("No")
    return

if __name__ == '__main__':
    main()