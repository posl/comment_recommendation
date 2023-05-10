def main():
    n,a,b = map(int,input().split())
    if n < 2:
        print(0)
        return
    if n == 2:
        print(1)
        return
    if a == 1:
        print(n)
        return
    if b == 1:
        print(n)
        return
    if n <= a:
        print(0)
        return
    if n <= b:
        print(0)
        return
    if a == 2:
        print(n-1)
        return
    if b == 2:
        print(n-1)
        return
    if a < b:
        print(n-a)
        return
    if b < a:
        print(n-b)
        return
    print(0)
    return

if __name__ == '__main__':
    main()