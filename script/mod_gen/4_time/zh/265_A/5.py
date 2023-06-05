def main():
    x, y, n = map(int, input().split())
    print((n//3)*2*y + (n%3)*x if n%3 != 0 else (n//3)*2*y)

if __name__ == '__main__':
    main()