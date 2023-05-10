def main():
    x = int(input())
    y = 100
    i = 0
    while x > y:
        y = y + int(y * 0.01)
        i += 1
    print(i)

if __name__ == '__main__':
    main()