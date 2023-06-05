def main():
    A, B = map(int, input().split())
    if A <= B:
        print(0)
    else:
        print(A - B * 2)

if __name__ == '__main__':
    main()