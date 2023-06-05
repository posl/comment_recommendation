def main():
    Y = int(input())
    while True:
        Y += 1
        if Y % 4 == 2:
            print(Y)
            break

if __name__ == '__main__':
    main()