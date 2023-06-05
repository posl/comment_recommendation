def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    sum = 0
    count = 0
    while sum < k:
        if len(a) > 0 and len(b) > 0:
            if a[0] < b[0]:
                if sum + a[0] <= k:
                    sum += a[0]
                    count += 1
                    a.pop(0)
                else:
                    break
            else:
                if sum + b[0] <= k:
                    sum += b[0]
                    count += 1
                    b.pop(0)
                else:
                    break
        elif len(a) > 0:
            if sum + a[0] <= k:
                sum += a[0]
                count += 1
                a.pop(0)
            else:
                break
        else:
            if sum + b[0] <= k:
                sum += b[0]
                count += 1
                b.pop(0)
            else:
                break
    print(count)
