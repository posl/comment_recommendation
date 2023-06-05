def main():
    s = input()
    k = int(input())
    x = 0
    y = 0
    z = 0
    for i in range(len(s)):
        if s[i] == 'X':
            x += 1
        else:
            y = max(y, x)
            x = 0
    y = max(y, x)
    for i in range(len(s)):
        if s[i] == '.':
            z += 1
    print(min(y + k, z))

if __name__ == '__main__':
    main()