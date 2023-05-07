def main():
    s = input()
    for i in range(0, len(s)):
        if (i % 2 == 0) and (s[i] == 'L'):
            print("No")
            return
        if (i % 2 == 1) and (s[i] == 'R'):
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()