def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    i,j = 0,0
    while i < n and j < m:
        ans = min(ans,abs(a[i]-b[j]))
        if a[i] == b[j]:
            break
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(ans)

if __name__ == '__main__':
    main()