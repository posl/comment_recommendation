def main():
    a, b, x = map(int, input().split())
    if x <= a**2*b/2:
        ans = math.degrees(math.atan(2*x/(a**3)))
    else:
        ans = math.degrees(math.atan((2*a**2*b-2*x)/(a**3)))
    print(ans)
