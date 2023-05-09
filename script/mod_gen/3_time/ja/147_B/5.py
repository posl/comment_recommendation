def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            count += 1
    print(count//2)

if __name__ == '__main__':
    main()