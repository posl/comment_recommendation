def solve():
    a, b, x = map(int, input().split())
    if x*2 <= a*a*b:
        print(90 - math.degrees(math.atan(2*x/(a*b*b))))
    else:
        print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))

if __name__ == '__main__':
    solve()