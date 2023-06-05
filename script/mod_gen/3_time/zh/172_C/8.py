def solve():
    # n,m,k = map(int,input().split())
    # a = list(map(int,input().split()))
    # b = list(map(int,input().split()))
    # a.sort()
    # b.sort()
    # time = 0
    # count = 0
    # while time <= k:
    #     if time+a[0] < time+b[0]:
    #         if time+a[0] <= k:
    #             count += 1
    #             time += a[0]
    #             a.pop(0)
    #         else:
    #             return count
    #     else:
    #         if time+b[0] <= k:
    #             count += 1
    #             time += b[0]
    #             b.pop(0)
    #         else:
    #             return count
    # return count
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    time = 0
    count = 0
    while time <= k:
        if len(a) == 0:
            if time+b[0] <= k:
                count += 1
                time += b[0]
                b.pop(0)
            else:
                return count
        elif len(b) == 0:
            if time+a[0] <= k:
                count += 1
                time += a[0]
                a.pop(0)
            else:
                return count
        else:
            if a[0] < b[0]:
                if time+a[0] <= k:
                    count += 1
                    time += a[0]
                    a.pop(0)
                else:
                    return count
            else:
                if time+b[0] <= k:
                    count += 1
                    time += b[0]
                    b.pop(0)
                else:
                    return count
    return count
print(solve())
