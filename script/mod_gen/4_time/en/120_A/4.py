def main():
    A, B, C = map(int, input().split())
    if B // A >= C:
        print(C)
    else:
        print(B // A)

if __name__ == '__main__':
    main()