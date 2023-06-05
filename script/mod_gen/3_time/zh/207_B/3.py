def main():
    a,b,c,d = map(int,input().split())
    if a < b:
        print(-1)
        return
    if b > c*d:
        print(-1)
        return
    if a <= c*d:
        print(1)
        return
    i = 1
    while a > c*d:
        a += b
        a -= c*d
        i += 1
    print(i)

if __name__ == '__main__':
    main()