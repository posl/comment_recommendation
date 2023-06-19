def main():
    A, B = map(int, input().split())
    if A >= B:
        print(A - B)
    else:
        print(0)

if __name__ == '__main__':
    main()