def main():
    a,b,c,d = map(int,input().split())
    if a <= b:
        print(-1)
        return
    if b <= c*d:
        print(-1)
        return
    count = 0
    while True:
        if a <= b:
            break
        if b <= c*d:
            break
        a += b
        count += 1
    print(count)

if __name__ == '__main__':
    main()