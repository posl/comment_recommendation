def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        if x[i]*x[i+k-1] >= 0:
            ans = min(ans, max(abs(x[i]), abs(x[i+k-1])))
        else:
            ans = min(ans, 2*min(abs(x[i]), abs(x[i+k-1])) + max(abs(x[i]), abs(x[i+k-1])))
    print(ans)

if __name__ == '__main__':
    main()