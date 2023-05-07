def main():
    a, b, c = map(int, input().split())
    tmp = a
    a = b
    b = tmp
    tmp = a
    a = c
    c = tmp
    print(a, b, c)

if __name__ == '__main__':
    main()