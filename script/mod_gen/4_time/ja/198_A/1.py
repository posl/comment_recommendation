def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(int((n-1)*n/2))

if __name__ == '__main__':
    main()