def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if b <= c or d <= a:
        print(0)
    else:
        print(max(b, d) - min(a, c))

if __name__ == '__main__':
    main()