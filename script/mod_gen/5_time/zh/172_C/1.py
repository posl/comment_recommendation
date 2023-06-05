def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = 0
    b_sum = 0
    for i in range(n):
        a_sum += a[i]
        if a_sum > k:
            a_sum -= a[i]
            break
    for i in range(m):
        b_sum += b[i]
        if b_sum > k:
            b_sum -= b[i]
            break
    ans = max(i,j)
    while i >= 0:
        b_sum += b[j]
        j += 1
        while b_sum > k and i >= 0:
            b_sum -= b[i]
            i -= 1
        ans = max(ans,i+j)
    print(ans)

if __name__ == '__main__':
    main()