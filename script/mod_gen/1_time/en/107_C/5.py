def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float("inf")
    for i in range(n-k+1):
        ans = min(ans, x[i+k-1]-x[i]+min(abs(x[i]), abs(x[i+k-1])))
    print(ans)

if __name__ == '__main__':
    main()