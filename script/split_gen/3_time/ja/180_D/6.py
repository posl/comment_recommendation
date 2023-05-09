def main():
    x,y,a,b = map(int,input().split())
    exp = 0
    while True:
        if x*a < x+b:
            if x*a >= y:
                break
            x *= a
            exp += 1
        else:
            if x+b >= y:
                break
            x += b
            exp += 1
    print(exp)
