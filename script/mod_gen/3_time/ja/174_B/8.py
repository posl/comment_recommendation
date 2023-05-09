def solve():
    # coding: utf-8
    # Your code here!
    import math
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    from collections import deque
    
    n,d = map(int,input().split())
    ans = 0
    for i in range(n):
        x,y = map(int,input().split())
        if math.sqrt(x**2 + y**2) <= d:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()