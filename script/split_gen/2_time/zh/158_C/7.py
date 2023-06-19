def solve(a,b):
    for i in range(1,101):
        if int(i*0.08) == a and int(i*0.1) == b:
            return i
    return -1
a,b = map(int,input().split())
print(solve(a,b))
