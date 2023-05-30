def main():
    a,b,d = map(int,input().split())
    import math
    d = math.radians(d)
    x = a*math.cos(d)-b*math.sin(d)
    y = a*math.sin(d)+b*math.cos(d)
    print(x,y)
main()
