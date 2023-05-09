def main():
    A, B = map(int, input().split())
    if B == 1:
        print(0)
    else:
        print((B+A-3)//(A-1))

if __name__ == '__main__':
    main()