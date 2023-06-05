def solve():
    h,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    s = sum(a)
    if s >= h:
        print("Yes")
    else:
        print("No")
