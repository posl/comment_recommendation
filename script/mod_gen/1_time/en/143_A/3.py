def main():
    a, b = map(int, input().split())
    print(0 if a >= b else b - a)

if __name__ == '__main__':
    main()