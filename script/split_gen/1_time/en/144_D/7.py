def main():
    a,b,x = map(int,input().split())
    if x < a**2*b/2:
        print(90-180/math.pi*math.atan(2*x/(a**3)))
    else:
        print(180-180/math.pi*math.atan(2*(a**2*b-x)/(a**3)))
