def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            y += 1
        else:
            x += 1
    print(x, y)

if __name__ == '__main__':
    main()