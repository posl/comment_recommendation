def main():
    A, B, C = map(int, input().split())
    if (B // A) < C:
        print(B // A)
    else:
        print(C)

if __name__ == '__main__':
    main()