def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    a_count = 0
    b_count = 0
    for i in range(n):
        if a_sum - a[i] <= k:
            a_count += 1
            a_sum -= a[i]
        else:
            break
    for j in range(m):
        if b_sum - b[j] <= k:
            b_count += 1
            b_sum -= b[j]
        else:
            break
    if a_count == n and b_count == m:
        print(n + m)
    elif a_count == n:
        print(n + b_count)
    elif b_count == m:
        print(m + a_count)
    else:
        print(max(a_count,b_count))
    return 0

if __name__ == '__main__':
    main()