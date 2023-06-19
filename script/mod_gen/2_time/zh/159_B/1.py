def main():
    s = input()
    n = len(s)
    if s == s[::-1]:
        if s[0:(n-1)//2] == s[0:(n-1)//2][::-1]:
            if s[(n+3)//2-1:n] == s[(n+3)//2-1:n][::-1]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()