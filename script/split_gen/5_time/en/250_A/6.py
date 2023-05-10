def main():
    h,w = map(int, input().split())
    r,c = map(int, input().split())
    print((h*w)-((h*c)+(w*r)-(r*c)))
