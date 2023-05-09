def max_diff(a,b,c,d):
    return max(a*c,a*d,b*c,b*d)
a,b = map(int, input().split())
c,d = map(int, input().split())
print(max_diff(a,b,c,d))
