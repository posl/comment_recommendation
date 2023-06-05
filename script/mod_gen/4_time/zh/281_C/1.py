def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    total = sum(a)
    t = t%total
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum >= t:
            print(i+1)
            break

if __name__ == '__main__':
    main()