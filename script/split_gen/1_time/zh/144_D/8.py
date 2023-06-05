def main():
    a,b,x = map(int,input().split())
    if x > a**2 * b / 2:
        ans = math.atan(2*(a**2*b-x)/(a**3))
    else:
        ans = math.atan((a*b**2)/(2*x))
    ans = math.degrees(ans)
    print(ans)
