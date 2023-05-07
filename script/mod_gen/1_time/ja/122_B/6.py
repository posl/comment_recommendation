def main():
    s = input()
    max_length = 0
    current_length = 0
    for i in range(len(s)):
        if s[i] in 'ACGT':
            current_length += 1
        else:
            current_length = 0
        max_length = max(max_length, current_length)
    print(max_length)

if __name__ == '__main__':
    main()