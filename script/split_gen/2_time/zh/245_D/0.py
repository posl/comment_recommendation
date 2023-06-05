def solve():
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    for i in range(n):
        if abs(a[i]-b[i])>k:
            print("No")
            return
    print("Yes")
    return
