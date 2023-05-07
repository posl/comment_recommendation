def main():
    s = input()
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c in s:
        if d[c] == 1:
            print(c)
            return
    print(-1)

if __name__ == '__main__':
    main()