def main():
    Y = int(input())
    while True:
        if Y % 4 == 2:
            print(Y)
            break
        Y += 1

if __name__ == '__main__':
    main()