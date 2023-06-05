def main():
    base = int(input())
    a, b = map(str, input().split())
    a = int(a, base)
    b = int(b, base)
    print(a*b)

if __name__ == '__main__':
    main()