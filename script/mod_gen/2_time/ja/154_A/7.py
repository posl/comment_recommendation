def solve():
    # -*- coding: utf-8 -*-
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(a,b)
solve()

if __name__ == '__main__':
    solve()