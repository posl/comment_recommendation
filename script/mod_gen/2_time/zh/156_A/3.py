def main():
    n,r = map(int,raw_input().split())
    if n < 10:
        print r + 100*(10-n)
    else:
        print r

if __name__ == '__main__':
    main()