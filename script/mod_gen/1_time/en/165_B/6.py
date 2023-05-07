def main():
    X = int(input())
    y = 100
    i = 0
    while y < X:
        y = int(y * 1.01)
        i += 1
    print(i)

if __name__ == '__main__':
    main()