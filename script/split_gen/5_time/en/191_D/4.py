def main():
    import math
    x,y,r = map(float, input().split())
    x1 = math.ceil(x-r)
    x2 = math.floor(x+r)
    ans = 0
    for i in range(x1,x2+1):
        y1 = math.ceil(y - math.sqrt(r**2 - (x-i)**2))
        y2 = math.floor(y + math.sqrt(r**2 - (x-i)**2))
        ans += y2 - y1 + 1
    print(ans)
main()
