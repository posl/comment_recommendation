def main():
    A, B = map(int, input().split())
    if A >= B * 2:
        print(A - B * 2)
    else:
        print(0)

if __name__ == '__main__':
    main()