def main():
    s = input()
    count = 0
    max_count = 0
    for i in range(len(s)):
        if s[i] == 'R':
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
    print(max_count)

if __name__ == '__main__':
    main()