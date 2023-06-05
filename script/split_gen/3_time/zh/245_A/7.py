def main():
    a,b,c,d = map(int,input().split())
    a = a*60 + b
    c = c*60 + d
    if a < c:
        print("高桥")
    else:
        print("青木")
