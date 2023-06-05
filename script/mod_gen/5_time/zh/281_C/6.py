def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    for i in range(n):
        count += a[i]
        if count >= t:
            print(i+1,t-(count-a[i]))
            break
    else:
        print((t-1)%n+1,t-(t-1)%n)

if __name__ == '__main__':
    main()