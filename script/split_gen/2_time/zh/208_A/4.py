def solve(a,b):
    if a*6 < b:
        return 'No'
    elif a <= b:
        return 'Yes'
    else:
        return 'No'
a,b = map(int,input().split())
print(solve(a,b))
