def main():
    X,Y = map(int,input().split())
    if Y % 10 == 0:
        if X <= Y:
            print(int((Y-X)/10))
        else:
            print(0)
    else:
        if X <= Y:
            print(int((Y-X)/10)+1)
        else:
            print(0)
