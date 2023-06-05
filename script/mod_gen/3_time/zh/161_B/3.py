def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum >= sum(a) * 0.25:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()