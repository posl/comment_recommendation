def main():
    s = input()
    n = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'v':
            n += 1
    print(n)

if __name__ == '__main__':
    main()