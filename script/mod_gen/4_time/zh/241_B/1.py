def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #a = sorted(a)
    #b = sorted(b)
    if m > n:
        print("No")
    else:
        #for i in range(m):
        #    if b[i] > a[i]:
        #        print("No")
        #        exit()
        #print("Yes")
        a.sort()
        b.sort()
        for i in range(m):
            if b[i] < a[i]:
                print("No")
                exit()
        print("Yes")

if __name__ == '__main__':
    main()