def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    #print(n, k)
    #print(x)
    ans = 10**9
    for i in range(n-k+1):
        #print(i)
        if x[i] <= 0 and x[i+k-1] <= 0:
            ans = min(ans, abs(x[i]))
        elif x[i] <= 0 and x[i+k-1] >= 0:
            ans = min(ans, abs(x[i])*2 + abs(x[i+k-1]))
        elif x[i] >= 0 and x[i+k-1] >= 0:
            ans = min(ans, abs(x[i+k-1]))
    print(ans)

if __name__ == '__main__':
    main()