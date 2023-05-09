def main():
    n = int(input())
    s = input()
    s = list(s)
    count = 0
    for i in range(n):
        if s[i] == '"':
            count += 1
        if s[i] == ',' and count % 2 == 1:
            s[i] = '.'
    print(''.join(s))

if __name__ == '__main__':
    main()