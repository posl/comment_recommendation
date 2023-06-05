def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    sum = 0
    for i in range(n-k+1):
        tmp = 0
        for j in range(i,i+k):
            tmp += p[j]
        sum = max(sum,tmp)
    print((sum+k)/2)

if __name__ == '__main__':
    main()