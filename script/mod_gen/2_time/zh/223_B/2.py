def main():
    s = input()
    s = s * 2
    length = len(s)
    min_s = s[:length//2]
    max_s = s[:length//2]
    for i in range(1, length//2):
        if min_s > s[i:i+length//2]:
            min_s = s[i:i+length//2]
        if max_s < s[i:i+length//2]:
            max_s = s[i:i+length//2]
    print(min_s)
    print(max_s)

if __name__ == '__main__':
    main()