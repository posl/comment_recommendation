def main():
    a, b, c = map(int, input().split())
    print(0 if a >= b + c else c - (a - b))

if __name__ == '__main__':
    main()