def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    total = sum(a)
    count = 0
    for i in range(m):
        if a[i]*4*m >= total:
            count += 1
    if count == m:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()