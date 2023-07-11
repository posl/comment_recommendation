def main():
    a,b,c,d,e,f,x = map(int, input().split())
    t = 0
    while True:
        if a > 0:
            x -= b
            t += a
        else:
            break
        if x <= 0:
            print("Takahashi")
            return
        if d > 0:
            x -= e
            t += d
        else:
            break
        if x <= 0:
            print("Aoki")
            return
    print("Draw")
