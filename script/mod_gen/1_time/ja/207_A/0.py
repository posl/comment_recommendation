def main():
    a, b, c = map(int, input().split())
    print(a + b + c - min(a, b, c))

if __name__ == '__main__':
    main()