def main():
    s = input()
    s_len = len(s)
    if s == s[::-1]:
        if s[:(s_len-1)//2] == s[:(s_len-1)//2][::-1]:
            if s[(s_len+3)//2-1:] == s[(s_len+3)//2-1:][::-1]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()