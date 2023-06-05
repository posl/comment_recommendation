def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    left = 1
    right = 2*n+1
    while True:
        mid = (left+right)//2
        print(mid)
        judge = int(input())
        if judge == 0:
            break
        if judge == -1:
            right = mid
        else:
            left = mid
    return
solve()
