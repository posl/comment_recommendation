def main():
    n,x,y = map(int,input().split())
    print(n,x,y)
    if n == 1:
        print(0)
        return 0
    if x == y:
        print((n-1)*x)
        return 0
    if x < y:
        print((n-1)*x)
        return 0
    if x > y:
        print((n-1)*y)
        return 0
