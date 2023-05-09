def main():
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        print(n*(n-1)//2)

if __name__ == '__main__':
    main()