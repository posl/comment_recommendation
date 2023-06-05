def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [i for i in a if i <= 0]
    a.reverse()
    b = list(map(lambda x: -x, a))
    a.extend(b)
    a = [0] + a
    #print(a)
    #print(n, k)
    l = 0
    r = 10 ** 18
    while l + 1 < r:
        mid = (l + r) // 2
        cnt = 0
        for i in range(1, n + 1):
            l1 = i
            r1 = n + 1
            while l1 + 1 < r1:
                mid1 = (l1 + r1) // 2
                if a[mid1] * a[i] <= mid:
                    l1 = mid1
                else:
                    r1 = mid1
            #print(l1)
            cnt += l1 - i
        #print(mid, cnt)
        if cnt < k:
            l = mid
        else:
            r = mid
    print(r)
solve()
