def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A <= 5:
        print(0)
    else:
        print(B // 2)

if __name__ == '__main__':
    main()