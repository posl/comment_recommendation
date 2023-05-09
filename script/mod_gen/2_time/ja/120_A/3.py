def main():
    A, B, C = map(int, input().split())
    if C * A > B:
        print(B // A)
    else:
        print(C)

if __name__ == '__main__':
    main()