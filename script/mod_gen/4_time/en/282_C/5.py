def main():
    n = int(input())
    s = input()
    s = list(s)
    for i in range(n):
        if i % 2 == 0:
            if s[i] == ',':
                s[i] = '.'
        else:
            if s[i] == '"':
                s[i] = ','
    print(''.join(s))

if __name__ == '__main__':
    main()