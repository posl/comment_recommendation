def solve():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 < l2:
        l1,l2 = l2,l1
        r1,r2 = r2,r1
    if l1 > r2:
        print(0)
    else:
        print(min(r1,r2)-l2)
