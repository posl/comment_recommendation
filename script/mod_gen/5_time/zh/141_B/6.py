def main():
    s = input()
    for i in range(0,len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                print("No")
                exit()
        else:
            if s[i] == 'R':
                print("No")
                exit()
    print("Yes")

if __name__ == '__main__':
    main()