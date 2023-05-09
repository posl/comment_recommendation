def main():
    a,b,c,d = map(int, input().split())
    if a <= b*d:
        print(-1)
        return
    for i in range(1,10**5+1):
        if a <= i*b:
            print(i)
            return

if __name__ == '__main__':
    main()