def main():
    a, b, c = map(int, input().split())
    print((a**2+b**2+c**2-a-b-c)/2/(a+b+c))

if __name__ == '__main__':
    main()