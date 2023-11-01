def main():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = (a+b)*c
    aoki = (d+e)*f
    if taka > aoki:
        print("Takahashi")
    elif taka < aoki:
        print("Aoki")
    else:
        print("Draw")
