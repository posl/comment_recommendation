def main():
    a,b,c,d,e,f,x = map(int,input().split())
    takahashi = 0
    aoki = 0
    for i in range(1,x+1):
        if i % (a+c) == 0:
            takahashi += b
        if i % (d+f) == 0:
            aoki += e
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()