def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        if x < a[0]:
            print(0)
        elif x >= a[-1]:
            print(n)
        else:
            l = 0
            r = n-1
            while l < r:
                mid = (l+r)//2
                if a[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            print(n-r)

if __name__ == '__main__':
    main()