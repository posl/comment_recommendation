def main():
    a = map(int, raw_input().split())
    n = 0
    for i in range(3):
        n = a[n]
    print n

if __name__ == '__main__':
    main()