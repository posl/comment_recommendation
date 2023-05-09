def main():
    a,b = map(int, input().split())
    a = str(a)
    b = str(b)
    if a * b < b * a:
        print(a * b)
    else:
        print(b * a)

if __name__ == '__main__':
    main()