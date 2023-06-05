def main():
    a,b = map(int,input().split())
    if b%a == 0:
        print(b//a - 1)
    else:
        print(b//a)

if __name__ == '__main__':
    main()