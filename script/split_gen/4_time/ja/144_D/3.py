def main():
    a, b, x = map(int, input().split())
    if a*a*b == x:
        print(0)
    elif x <= a*a*b/2:
        print(90 - math.degrees(math.atan(2*x/(a*b*b))))
    else:
        print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))
