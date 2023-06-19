def main():
    r,x,y = map(int,input().split())
    if r*r == x*x + y*y:
        print(1)
    elif r*r > x*x + y*y:
        print(2)
    else:
        count = 0
        while r*r < x*x + y*y:
            x -= r
            count += 1
        print(count+1)
