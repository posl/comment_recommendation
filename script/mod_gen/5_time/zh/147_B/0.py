def main():
    s = input()
    count = 0
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-1-i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()