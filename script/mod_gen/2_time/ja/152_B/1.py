def main():
    a, b = map(int, input().split())
    x = str(a) * b
    y = str(b) * a
    if x < y:
        print(x)
    else:
        print(y)

if __name__ == '__main__':
    main()