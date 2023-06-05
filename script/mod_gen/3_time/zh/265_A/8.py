def main():
    x,y,n = map(int,input().split())
    if n % 3 == 0:
        print(y * (n // 3))
    elif n % 3 == 1:
        print(y * (n // 3) + x)
    else:
        print(y * (n // 3) + x * 2)

if __name__ == '__main__':
    main()