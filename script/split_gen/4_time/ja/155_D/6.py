def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = -10**18
    r = 10**18
    while (r - l) > 1:
        mid = (l + r) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                #print('a[i] < 0')
                l = mid
                continue
            #print('a[i] >= 0')
            if a[i] == 0:
                if mid >= 0:
                    cnt += n - i - 1
            else:
                if a[i] * a[-1] <= mid:
                    cnt += n - i - 1
                else:
                    l = mid
                    continue
            #print('cnt = ' + str(cnt))
            low = i + 1
            high = n - 1
            while (high - low) > 1:
                mid2 = (low + high) // 2
                if a[i] * a[mid2] <= mid:
                    low = mid2
                else:
                    high = mid2
            cnt += low - i
            #print('cnt = ' + str(cnt))
        if cnt < k:
            l = mid
        else:
            r = mid
    print(r)
