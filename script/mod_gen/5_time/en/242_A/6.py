def main():
    a, b, c, x = map(int, input().split())
    print((c/b) if a <= x <= b else 0 if x < a else 1)

if __name__ == '__main__':
    main()