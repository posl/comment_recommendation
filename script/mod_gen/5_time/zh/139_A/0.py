def main():
    s = input()
    t = input()
    n = 0
    for i in range(3):
        if s[i] == t[i]:
            n += 1
    print(n)

if __name__ == '__main__':
    main()