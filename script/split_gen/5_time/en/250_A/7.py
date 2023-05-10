def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print((h*w)-((r*w)+(c*h)-(r*c)))
