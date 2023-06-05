def get_input():
    n,m = map(int,input().split())
    a = [0] * m
    for i in range(m):
        a[i] = int(input())
    return n,m,a
