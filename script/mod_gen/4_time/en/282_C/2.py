def main():
    n = int(input())
    s = input()
    s = list(s)
    for i in range(n):
        if s[i] == ',':
            if i % 2 == 0:
                s[i] = '.'
    print(''.join(s))

if __name__ == '__main__':
    main()