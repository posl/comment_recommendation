def main():
    a,b,c,x = map(int,input().split())
    if a <= x and x <= b:
        print(c/b)
    else:
        print(0)
