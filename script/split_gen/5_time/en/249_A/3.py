def main():
    a,b,c,d,e,f,x = map(int, input().split())
    t = 0
    aoki = 0
    takahashi = 0
    while t < x:
        if t % (a + b) < a:
            takahashi += c
        if t % (d + e) < d:
            aoki += f
        t += 1
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")
