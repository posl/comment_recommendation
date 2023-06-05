def main():
    x,y,z = map(int,input().split())
    if y > 0:
        print(-1)
    else:
        print(abs(x)+abs(z))
