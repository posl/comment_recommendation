def main():
    a,b,x = map(int, input().split())
    if x >= a*a*b/2:
        ans = 90 - math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))
    else:
        ans = math.degrees(math.atan(a*b*b/(2*x)))
    print(ans)

if __name__ == '__main__':
    main()