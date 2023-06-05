def main():
    x, y, n = map(int, input().split())
    print(int((n+y-1)/y*x))

if __name__ == '__main__':
    main()