def main():
    A, B = map(int, input().split())
    if A >= 15 and B >= 8:
        print(1)
    elif A >= 10 and B >= 3:
        print(2)
    elif A >= 3:
        print(3)
    else:
        print(4)

if __name__ == '__main__':
    main()