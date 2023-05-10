def main():
    a, b, n = map(int, input().split())
    if n < b:
        x = n
    else:
        x = b - 1
    print(int(a*x/b) - a*int(x/b))

if __name__ == '__main__':
    main()