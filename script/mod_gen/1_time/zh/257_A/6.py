def main():
    n, x = map(int, input().split())
    print(chr((x-1)//n + 65))

if __name__ == '__main__':
    main()