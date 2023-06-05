def main():
    a, b, c = map(int, input().split())
    print(max(a+b, b+c, a+c))

if __name__ == '__main__':
    main()