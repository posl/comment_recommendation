def main():
    a,b,c,d,e,f,x = map(int, input().split())
    t = 0
    while x > 0:
        if a > 0:
            x -= b
            t += a
        if x <= 0:
            break
        x -= c
        if d > 0:
            t -= d
        if x <= 0:
            break
        x -= e
        t += f
    if t > 0:
        print("Takahashi")
