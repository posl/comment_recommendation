def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    for i in range(q):
        l,r,x = map(int,input().split())
        cnt = 0
        for j in range(l-1,r):
            if a[j] == x:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()