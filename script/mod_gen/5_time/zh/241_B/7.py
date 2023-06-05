def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if n < m:
        print('No')
        return
    a.sort(reverse=True)
    b.sort(reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] >= b[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == m:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()