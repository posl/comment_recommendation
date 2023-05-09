def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if a <= c <= b:
        print(max(b - c, d - a))
    elif c <= a <= d:
        print(max(b - c, d - a))
    else:
        print(max(b - a, d - c))

if __name__ == '__main__':
    main()