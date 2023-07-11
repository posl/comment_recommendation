def main():
    a,b,c,d,e,f,x = map(int, input().split())
    t = 0
    while True:
        if a > 0:
            x -= b
            if x <= 0:
                print("Takahashi")
                break
            x += c
            if x <= 0:
                print("Aoki")
                break
        if d > 0:
            x -= e
            if x <= 0:
                print("Takahashi")
                break
            x
