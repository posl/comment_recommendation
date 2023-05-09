def main():
    x,y,z = map(int,input().split())
    if x > 0:
        if z < y:
            print(x - y)
        else:
            print(-1)
    else:
        if z < y:
            print(y - x)
        else:
            print(-1)
