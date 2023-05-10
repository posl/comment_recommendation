def main():
    a,b,x = map(int, input().split())
    if x > a*a*b/2:
        print(90 - math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))
    else:
        print(math.degrees(math.atan((a*b*b)/(2*x))))
