def solve():
    a,b,x = map(int,input().split())
    if x == a*a*b:
        print(0)
    else:
        if x <= a*a*b/2:
            print(90-math.degrees(math.atan2((a*b*b)/2,x)))
        else:
            print(math.degrees(math.atan2((2*(a*a*b-x))/(a*a),a)))
