def main():
    n, l = map(int, input().split())
    #print(n, l)
    a = [i for i in range(l, l+n)]
    #print(a)
    if 0 in a:
        print(sum(a))
    elif l > 0:
        print(sum(a)-a[0])
    elif l < 0 and l+n-1 >= 0:
        print(sum(a)-a[-1])
    else:
        print(sum(a)-a[-1])

if __name__ == '__main__':
    main()