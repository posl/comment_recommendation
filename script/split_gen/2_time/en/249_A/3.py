def main():
    a,b,c,d,e,f,x = map(int, input().split())
    takahashi = b * (a + c)
    aoki = e * (d + f)
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")
