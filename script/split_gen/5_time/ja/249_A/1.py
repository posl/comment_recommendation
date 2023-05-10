def main():
    a,b,c,d,e,f,x = map(int, input().split())
    t = 0
    while True:
        if t >= x:
            break
        else:
            t += a
            if t >= x:
                break
            else:
                t += d
    print("Takahashi" if t >= x else "Aoki")
