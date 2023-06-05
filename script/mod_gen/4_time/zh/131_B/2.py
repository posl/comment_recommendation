def main():
    n,l = map(int,input().split())
    min_sum = 1000000000
    for i in range(1,n+1):
        if abs(l+i-1) < abs(min_sum):
            min_sum = l+i-1
    print(sum(range(l+1,l+n))-min_sum)

if __name__ == '__main__':
    main()