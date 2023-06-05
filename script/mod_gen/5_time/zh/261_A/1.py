def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 < l2:
        if r1 < l2:
            print(0)
        else:
            print(min(r1,r2) - l2)
    else:
        if r2 < l1:
            print(0)
        else:
            print(min(r1,r2) - l1)

if __name__ == '__main__':
    main()