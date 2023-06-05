def main():
    x,y = map(int,input().split())
    if x >= y:
        print(0)
        return
    else:
        print((y-x)//10)
