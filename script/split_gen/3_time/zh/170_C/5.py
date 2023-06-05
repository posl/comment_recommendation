def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    if n == 0:
        print(x)
        return
    if n == 1:
        if p[0] == x:
            print(x+1)
        else:
            print(x)
        return
    if x not in p:
        print(x)
        return
    for i in range(1,x):
        if i not in p:
            print(i)
            return
    print(x+1)
