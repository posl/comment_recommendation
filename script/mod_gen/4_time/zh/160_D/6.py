def main():
    n,x,y = [int(x) for x in input().split()]
    n1 = y-x-1
    n2 = n-y+x-1
    n3 = n-n2-1
    n4 = n-n1-1
    n5 = n-1
    print(n5)
    print(n4)
    print(n3)
    print(n2)
    print(n1)
    print(0)
    print(0)
    print(0)
    print(0)
    print(0)

if __name__ == '__main__':
    main()