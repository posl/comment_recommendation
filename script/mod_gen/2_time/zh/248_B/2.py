def main():
    a,b,k = map(int,input().split())
    c = 0
    while a < b:
        a += a * (k - 1)
        c += 1
    print(c)

if __name__ == '__main__':
    main()