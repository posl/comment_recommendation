def main():
    s = input()
    l = len(s)
    count = 0
    for i in range(int(l/2)):
        if s[i] != s[l-i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()