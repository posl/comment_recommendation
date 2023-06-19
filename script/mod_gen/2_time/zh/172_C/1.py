def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum+b_sum <= k:
        print(n+m)
    else:
        b_sum = 0
        count = 0
        for i in range(n):
            b_sum += a[i]
            if b_sum <= k:
                count += 1
            else:
                break
        a_sum = 0
        for i in range(m):
            a_sum += b[i]
            if a_sum <= k:
                count += 1
            else:
                break
        print(count)

if __name__ == '__main__':
    main()