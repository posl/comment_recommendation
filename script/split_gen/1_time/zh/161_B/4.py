def problems161_b():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum_a = sum(a)
    if a[m-1] >= sum_a / (4*m):
        print("Yes")
    else:
        print("No")
