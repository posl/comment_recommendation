def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k == 1:
        print(n)
        return
    if k == n:
        print(1)
        return
    if n == 2:
        if a[0] == a[1]:
            print(1)
        else:
            print(2)
        return
    if k == 2:
        a = list(set(a))
        cnt = 0
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                cnt += 1
        print(n-cnt)
        return
    if k == 3:
        a = list(set(a))
        cnt = 0
        for i in range(len(a)-2):
            if a[i] == a[i+1]-1 and a[i+1] == a[i+2]-1:
                cnt += 1
        print(n-cnt)
        return

if __name__ == '__main__':
    main()