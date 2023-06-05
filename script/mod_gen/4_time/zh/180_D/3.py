def main():
    x,y,a,b = map(int,input().split())
    exp = 0
    if a == 1:
        exp = (y-x)//b
        if (y-x) % b == 0:
            exp -= 1
        print(exp)
        return
    while True:
        if x*a < x+b:
            if x*a < y:
                x *= a
                exp += 1
            else:
                print(exp)
                return
        else:
            if x+b < y:
                x += b
                exp += 1
            else:
                print(exp)
                return
main()
