def main():
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    print(a+b+c-max(a,b,c))

if __name__ == '__main__':
    main()