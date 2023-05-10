def main():
    x,y = map(int,input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    if x>y:
        x,y = y,x
    if x*2 < y:
        print(0)
        return
    if x==y:
        print(2)
        return
    print(1)
    return
