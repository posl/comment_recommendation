def problem141c():
    n,k,q = map(int,input().split())
    a = [int(input()) for _ in range(q)]
    result = [0 for _ in range(n)]
    for i in range(q):
        result[a[i]-1] += 1
    for i in range(n):
        if k - q + result[i] > 0:
            print("Yes")
        else:
            print("No")
