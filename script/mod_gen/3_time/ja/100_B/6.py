def main():
    d,n = map(int, input().split())
    if n == 100:
        n += 1
    print(100**d*n)
main()

if __name__ == '__main__':
    main()