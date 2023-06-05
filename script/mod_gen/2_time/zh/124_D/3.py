def main():
    s = input()
    s = s.strip()
    if len(s) == 1:
        print(0)
        return
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()