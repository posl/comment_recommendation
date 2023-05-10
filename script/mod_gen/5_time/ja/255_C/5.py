def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print("inf")
    else:
        if (x-a)%d == 0:
            if (x-a)//d >= 0:
                print((x-a)//d+1)
            else:
                print("inf")
        else:
            print("inf")

if __name__ == '__main__':
    main()