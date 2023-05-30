def main():
    a, b, h, m = map(int, input().split())
    angle = abs((h*60+m)/2 - m*6)
    import math
    ans = math.sqrt(a*a + b*b - 2*a*b*math.cos(math.radians(angle)))
    print(ans)
main()
