def solve():
    a = list(map(int,input().split()))
    a.sort()
    count = 0
    for i in range(4):
        if a[i] == 100:
            count += 1
    if count == 2:
        print("YES")
    else:
        print("NO")
