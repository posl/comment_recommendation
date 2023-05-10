def main():
    n,m = map(int, input().split())
    if m == 0:
        print(n)
        return
    else:
        print(n*(n-1)//2 - m)

if __name__ == '__main__':
    main()