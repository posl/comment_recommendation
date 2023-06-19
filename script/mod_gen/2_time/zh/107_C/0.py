def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(n-k+1):
        if x[i] <= 0 <= x[i+k-1]:
            ans = min(ans, min(abs(x[i]),abs(x[i+k-1]))*2 + max(abs(x[i]),abs(x[i+k-1])))
        elif x[i] < 0:
            ans = min(ans, abs(x[i]) + x[i+k-1])
        else:
            ans = min(ans, x[i+k-1] + abs(x[i]))
    print(ans)

if __name__ == '__main__':
    main()