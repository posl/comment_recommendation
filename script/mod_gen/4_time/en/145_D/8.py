def main():
    x,y = map(int,input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    n = (x+y)//3
    if max(x,y) > n:
        print(0)
        return
    print(comb(n,x))

if __name__ == '__main__':
    main()