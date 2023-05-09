def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    tmp = sum(p[:k])
    ans = max(ans, tmp)
    for i in range(n-k):
        tmp += p[i+k] - p[i]
        ans = max(ans, tmp)
    print((ans+k)/2)

if __name__ == '__main__':
    main()