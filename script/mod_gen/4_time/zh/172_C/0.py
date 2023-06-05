def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    sum = 0
    time = 0
    a_index = 0
    b_index = 0
    while time <= k and a_index < n and b_index < m:
        if a[a_index] <= b[b_index]:
            time += a[a_index]
            if time <= k:
                sum += 1
                a_index += 1
            else:
                break
        else:
            time += b[b_index]
            if time <= k:
                sum += 1
                b_index += 1
            else:
                break
    if a_index == n and b_index < m:
        while time <= k and b_index < m:
            time += b[b_index]
            if time <= k:
                sum += 1
                b_index += 1
            else:
                break
    elif b_index == m and a_index < n:
        while time <= k and a_index < n:
            time += a[a_index]
            if time <= k:
                sum += 1
                a_index += 1
            else:
                break
    print(sum)

if __name__ == '__main__':
    main()