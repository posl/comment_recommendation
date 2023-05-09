def main():
    a,b,c,d,e,f,x = map(int,input().split())
    takahashi = (a+b)*x//b
    aoki = (d+e)*x//e
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")
