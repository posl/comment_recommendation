def main():
    a,b,c = map(int, input().split())
    if c * a <= b:
        print(c)
    else:
        print(b // a)

if __name__ == '__main__':
    main()