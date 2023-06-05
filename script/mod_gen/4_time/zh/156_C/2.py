def main():
    n = int(input())
    x = input().split()
    x = [int(x[i]) for i in range(n)]
    x.sort()
    ans = 10**18
    for i in range(x[0],x[-1]+1):
        sum = 0
        for j in range(n):
            sum += (x[j]-i)**2
        ans = min(ans,sum)
    print(ans)

if __name__ == '__main__':
    main()