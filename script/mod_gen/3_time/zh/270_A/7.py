def main():
    A,B = map(int, input().split())
    if A >= 4:
        A -= 4
    if B >= 4:
        B -= 4
    print(7 - A - B)

if __name__ == '__main__':
    main()