def main():
    a,b,x = map(int,input().split())
    if x*2 >= a**2*b:
        print(90)
    else:
        print(90 - math.degrees(math.atan(2*x/(a*b**2))))
