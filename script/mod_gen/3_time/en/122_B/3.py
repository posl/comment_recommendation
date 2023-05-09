def main():
    s = input()
    count = 0
    max_count = 0
    for i in range(len(s)):
        if s[i] in 'ACGT':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)
main()

if __name__ == '__main__':
    main()