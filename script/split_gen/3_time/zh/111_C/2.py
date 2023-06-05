def solve():
    n = int(input())
    v = list(map(int,input().split()))
    a = [0]*100001
    b = [0]*100001
    for i in range(n):
        if i % 2 == 0:
            a[v[i]] += 1
        else:
            b[v[i]] += 1
    a_max = max(a)
    b_max = max(b)
    if a_max == b_max:
        if a_max == n//2:
            print(n//2)
        else:
            print(n//2)
    else:
        print(n-a_max-b_max)
