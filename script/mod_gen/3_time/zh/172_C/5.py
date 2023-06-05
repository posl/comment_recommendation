def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum + b_sum <= k:
        print(n+m)
        return
    a_sum = 0
    b_sum = 0
    a_index = 0
    b_index = 0
    count = 0
    while a_sum + b_sum <= k:
        if a_sum < b_sum:
            a_sum += a[a_index]
            a_index += 1
        else:
            b_sum += b[b_index]
            b_index += 1
        count += 1
        if a_index == n or b_index == m:
            break
    if a_sum + b_sum <= k:
        print(n+m)
        return
    if a_sum < b_sum:
        b_sum -= b[b_index - 1]
        b_index -= 1
    else:
        a_sum -= a[a_index - 1]
        a_index -= 1
    count -= 1
    while a_index >= 0 and b_index >= 0:
        if a_sum < b_sum:
            a_sum += a[a_index]
            a_index -= 1
        else:
            b_sum += b[b_index]
            b_index -= 1
        count += 1
    print(count)

if __name__ == '__main__':
    main()