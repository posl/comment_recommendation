def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    for c in s:
        if c == 'S':
            x += 1
        else:
            y += 1
    print(x, y)

if __name__ == '__main__':
    main()