def main():
    s = input()
    print((s[0] != s[1]) + sum(i != j for i, j in zip(s, s[1:])))

if __name__ == '__main__':
    main()