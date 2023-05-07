def main():
    n,m = map(int,input().split())
    if n == 0 or m == 0:
        print(0)
        return
    if n == 1 and m == 1:
        print(0)
        return
    if n == 1:
        print(m)
        return
    if m == 1:
        print(n)
        return
    print(n*m-n-m+1)
    return

if __name__ == '__main__':
    main()