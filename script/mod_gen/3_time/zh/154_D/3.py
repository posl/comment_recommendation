def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    p_sum = [0]
    for i in range(1,n+1):
        p_sum.append(p_sum[i-1]+p[i])
    ans = 0
    for i in range(k, n+1):
        ans = max(ans, p_sum[i]-p_sum[i-k])
    print(ans/2)

if __name__ == '__main__':
    main()