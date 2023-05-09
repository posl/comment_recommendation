def main():
    x,y,n = map(int,input().split())
    if x*3 > y:
        print(int(y*(n/3)))
    else:
        print(int(x*n))
