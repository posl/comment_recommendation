def solve():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a,b = input().split()
        s.append(a)
        t.append(b)
    if len(set(s)) == n and len(set(t)) == n and len(set(s) & set(t)) == 0:
        print('Yes')
    else:
        print('No')
