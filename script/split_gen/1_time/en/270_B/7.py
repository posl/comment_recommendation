def main():
    x,y,z = map(int,input().split())
    if z > y:
        print(x-z)
    else:
        print(-1)
