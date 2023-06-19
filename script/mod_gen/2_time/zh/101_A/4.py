def main():
    s = input()
    n = 0
    for c in s:
        if c == '+':
            n += 1
        else:
            n -= 1
    print(n)

if __name__ == '__main__':
    main()