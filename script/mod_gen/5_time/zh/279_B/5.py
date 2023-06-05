def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i:len(t)+i] == t:
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()