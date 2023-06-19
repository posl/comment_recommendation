def solve():
    x,y,n = map(int,input().split())
    result = 0
    for i in range(1,n+1):
        if i%3 == 0:
            result += x
        else:
            result += y
    print(result)
