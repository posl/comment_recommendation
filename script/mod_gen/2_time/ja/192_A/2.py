def main():
    X = int(input())
    if X % 100 == 0:
        print(100)
    else:
        print(100 - (X % 100))

if __name__ == '__main__':
    main()