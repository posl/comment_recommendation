def main():
    a,b,c = map(int, input().split())
    print(c if a >= b+c else b+c-a)

if __name__ == '__main__':
    main()