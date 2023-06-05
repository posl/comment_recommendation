def main():
    a = input().split()
    p = int(a[0])
    q = int(a[1])
    r = int(a[2])
    print(min(p+q,q+r,r+p))

if __name__ == '__main__':
    main()