def main():
    A, B = map(int, input().split())
    if A >= B:
        print(1)
    else:
        print(B - A + 1)

if __name__ == '__main__':
    main()