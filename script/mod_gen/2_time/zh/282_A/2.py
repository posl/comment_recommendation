def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    if k == 1:
        if sum % d == 0:
            print(sum)
        else:
            print(-1)
        return
    if k == n:
        if sum % d == 0:
            print(0)
        else:
            print(-1)
        return
    if k == 2:
        ans = -1
        for i in range(n):
            for j in range(i+1,n):
                if (sum - a[i] - a[j]) % d == 0:
                    ans = max(ans,sum - a[i] - a[j])
        print(ans)
        return
    if k == 3:
        ans = -1
        for i in range(n):
            for j in range(i+1,n):
                for m in range(j+1,n):
                    if (sum - a[i] - a[j] - a[m]) % d == 0:
                        ans = max(ans,sum - a[i] - a[j] - a[m])
        print(ans)
        return
    if k == 4:
        ans = -1
        for i in range(n):
            for j in range(i+1,n):
                for m in range(j+1,n):
                    for p in range(m+1,n):
                        if (sum - a[i] - a[j] - a[m] - a[p]) % d == 0:
                            ans = max(ans,sum - a[i] - a[j] - a[m] - a[p])
        print(ans)
        return
    if k == 5:
        ans = -1
        for i in range(n):
            for j in range(i+1,n):
                for m in range(j+1,n):
                    for p in range(m+1,n):
                        for q in range(p+1,n):
                            if (sum - a[i] - a[j] - a[m] - a[p] - a[q]) % d == 0:
                                ans = max(ans,sum - a[i] - a[j] - a[m] - a[p] - a[q])
        print(ans)
        return
    if k == 6:
        ans = -1

if __name__ == '__main__':
    main()