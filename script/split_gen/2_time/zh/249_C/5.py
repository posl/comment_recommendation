def get_input():
    n,k = map(int,input().split())
    s = []
    for i in range(n):
        s.append(input())
    return n,k,s
