def main():
    n,k = map(int,input().split())
    sum = 0
    for a in range(1,n+1):
        if a%k == 0:
            sum += n//k
        elif k%2 == 0 and a%k == k//2:
            sum += n//k
        else:
            sum += n//k+1
    print(sum)

if __name__ == '__main__':
    main()