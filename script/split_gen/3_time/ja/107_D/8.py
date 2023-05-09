def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = []
    for i in range(n):
        for j in range(i,n):
            m.append(a[i:j+1])
    m.sort()
    print(m[len(m)//2])
