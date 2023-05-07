def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = [0]*(n+1)
    for i in range(n):
        sum_a[i+1] = sum_a[i] + a[i]
    ans = -float('inf')
    for i in range(n-m+1):
        for j in range(i+m, n+1):
            ans = max(ans, sum_a[j]-sum_a[i] + (j-i)*sum(a[i:j]))
    print(ans)

if __name__ == '__main__':
    main()