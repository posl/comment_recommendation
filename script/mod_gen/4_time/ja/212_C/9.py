def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    a_index = 0
    b_index = 0
    min_diff = 10**9+1
    while a_index < n and b_index < m:
        diff = abs(a[a_index] - b[b_index])
        if diff < min_diff:
            min_diff = diff
        if a[a_index] < b[b_index]:
            a_index += 1
        else:
            b_index += 1
    print(min_diff)

if __name__ == '__main__':
    main()