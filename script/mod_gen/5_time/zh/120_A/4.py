def solve():
    a,b,c = map(int,input().split())
    return min(b//a,c)
print(solve())
