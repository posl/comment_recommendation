def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    sum_a = sum(a)
    for i in range(n):
        sum_a -= a[i]
        ans += (n-1)*a[i]**2 - 2*a[i]*sum_a
    print(ans)

if __name__ == '__main__':
    main()