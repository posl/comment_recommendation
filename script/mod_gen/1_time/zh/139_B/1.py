def main():
    a,b = map(int, input().split())
    if b%a == 0:
        print(0)
    else:
        print(a-b%a)

if __name__ == '__main__':
    main()