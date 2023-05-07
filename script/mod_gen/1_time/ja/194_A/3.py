def main():
    A, B = map(int, input().split())
    if 15 <= A+B:
        print(1)
    elif 10 <= A+B:
        print(2)
    elif 3 <= A+B:
        print(3)
    else:
        print(4)

if __name__ == '__main__':
    main()