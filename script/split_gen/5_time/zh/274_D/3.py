def solve():
    n,x,y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.insert(0,0)
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if a[i] + a[j] == abs(x-y):
                if (x > y and i > j) or (x < y and i < j):
                    print("No")
                    return
    print("Yes")
