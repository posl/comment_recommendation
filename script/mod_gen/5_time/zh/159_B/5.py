def main():
    s = input()
    if s == s[::-1]:
        if s[0:(len(s)-1)//2] == s[0:(len(s)-1)//2][::-1]:
            if s[(len(s)+3)//2-1:len(s)] == s[(len(s)+3)//2-1:len(s)][::-1]:
                print("Yes")
                exit()
    print("No")

if __name__ == '__main__':
    main()