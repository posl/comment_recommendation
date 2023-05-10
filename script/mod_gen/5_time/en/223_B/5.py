def main():
    s = input()
    n = len(s)
    s = s+s
    print(min([s[i:i+n] for i in range(n)]))
    print(max([s[i:i+n] for i in range(n)]))

if __name__ == '__main__':
    main()