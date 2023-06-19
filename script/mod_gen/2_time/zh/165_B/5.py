def main():
    x = int(input())
    y = 100
    i = 0
    while y < x:
        i += 1
        y += y // 100
    print(i)

if __name__ == '__main__':
    main()