def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a <= 5:
        print(0)
    else:
        print(int(b/2))

if __name__ == '__main__':
    main()