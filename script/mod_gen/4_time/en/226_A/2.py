def main():
    X = float(input())
    if X % 1 >= 0.5:
        print(int(X + 1))
    else:
        print(int(X))

if __name__ == '__main__':
    main()