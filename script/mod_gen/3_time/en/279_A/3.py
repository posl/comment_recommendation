def main():
    s = input()
    count = 0
    for i in range(1,len(s)):
        if s[i] == 'v' and s[i-1] == 'v':
            count += 1
    print(count)

if __name__ == '__main__':
    main()