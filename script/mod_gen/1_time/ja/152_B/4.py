def main():
    a, b = map(int, input().split())
    if a * b == 0:
        print(0)
        return
    elif a < b:
        print(str(a) * b)
    elif a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)

if __name__ == '__main__':
    main()